import fs from 'node:fs';
import {createClient,createAccount,generatePrivateKey} from 'genlayer-js';
import {studionet} from 'genlayer-js/chains';
import {example,missing} from '../src/example.js';
fs.mkdirSync('.local',{recursive:true});fs.mkdirSync('evidence',{recursive:true});
if(!fs.existsSync('.local/signer'))fs.writeFileSync('.local/signer',generatePrivateKey(),{mode:0o600});
const account=createAccount(fs.readFileSync('.local/signer','utf8').trim());
const client=createClient({chain:studionet,account,endpoint:'https://studio.genlayer.com/api'});
const save=(f,x)=>fs.writeFileSync(f,JSON.stringify(x,(_,v)=>typeof v==='bigint'?v.toString():v,2));
const code=fs.readFileSync('contracts/cueloom.py','utf8');
const d=fs.existsSync('deployment.json')?JSON.parse(fs.readFileSync('deployment.json','utf8')):{network:'Stable Studionet',chainId:61999,owner:account.address.toLowerCase(),calls:[]};
const [action,...args]=process.argv.slice(2);
if(action==='schema')console.log(JSON.stringify(await client.getContractSchemaForCode(code)));
if(action==='deploy'){if(d.deployHash)throw Error('Already submitted');d.deployHash=await client.deployContract({code,args:[],leaderOnly:false});save('deployment.json',d);console.log(d.deployHash);}
if(action==='receipt'){const hash=args[0]||d.deployHash;const tx=await client.getTransaction({hash});save('evidence/'+hash+'.json',tx);console.log(JSON.stringify({status:tx.status,result:tx.result,execution:tx.execution_result,address:tx.to_address,contractAddress:tx.contract_address}));}
if(action==='address'){d.address=args[0];save('deployment.json',d);console.log('protocol',await client.readContract({address:d.address,functionName:'protocol',args:[]}));console.log('sourceMatch',await client.getContractCode(d.address)===code);}
if(action==='send'){const method=args[0];const params=JSON.parse(args[1]);const hash=await client.writeContract({address:d.address,functionName:method,args:params,value:0n,leaderOnly:false});d.calls.push({method,args:params,hash});save('deployment.json',d);console.log(hash);}
if(action==='example'){const p=args[1]==='missing'?missing:example;const params=[args[0],JSON.stringify(p)];const hash=await client.writeContract({address:d.address,functionName:'seal',args:params,value:0n,leaderOnly:false});d.calls.push({method:'seal',args:params,hash});save('deployment.json',d);console.log(hash);}
if(action==='read'){const raw=await client.readContract({address:d.address,functionName:'read',args:[args[1]||d.owner,args[0]],transactionHashVariant:'latest-final'});if(raw){const r=JSON.parse(raw);save('evidence/'+args[0]+'.json',r);console.log(JSON.stringify(r));}else console.log('null');}
