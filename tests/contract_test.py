import sys, types, json, unittest
from pathlib import Path
class Return:
    def __init__(self, value): self.calldata = value
sender = types.SimpleNamespace(sender_address='0x'+'1'*40)
answers=[]
def prompt(*args, **kwargs): return {'labels': answers.pop(0)}
def run(fn, validator):
    result=fn()
    assert validator(Return(result)), 'DISAGREEMENT'
    return result
gl=types.SimpleNamespace(Contract=object, public=types.SimpleNamespace(write=lambda f:f,view=lambda f:f),message=sender,nondet=types.SimpleNamespace(exec_prompt=prompt),vm=types.SimpleNamespace(Return=Return,run_nondet_unsafe=run))
fake=types.ModuleType('genlayer');fake.gl=gl;fake.TreeMap=dict
sys.modules['genlayer']=fake
ns={};exec(Path('contracts/cueloom.py').read_text(),ns)
p={'title':'Small studio','source_language':'English','target_language':'Chinese','source':[{'start':0,'end':2000,'text':'We open at nine.'},{'start':2500,'end':4000,'text':'Bring paper.'},{'start':4500,'end':6000,'text':'Ink is free.'}],'target':['九点开门。','自带纸张，油墨免费。']}
class Tests(unittest.TestCase):
 def setUp(self):
  sender.sender_address='0x'+'1'*40;answers.clear()
 def contract(self):
  c=ns['CueLoom']();c.reels={};c.seal('studio',json.dumps(p));return c
 def labels(self):
  return ['E' if e in [[0,0,1,1],[1,1,2,1]] else 'N' for e in ns['blocks'](p)]
 def test_complete_merge_and_export(self):
  c=self.contract();a=self.labels();answers.extend([a,a]);c.align('studio');r=json.loads(c.read(sender.sender_address,'studio'));self.assertEqual(len(r['paths']),1);c.publish('studio',r['alignment_hash'],0);r=json.loads(c.read(sender.sender_address,'studio'));self.assertIn('00:00:02.500 --> 00:00:06.000',r['vtt']);self.assertEqual(r['phase'],'PUBLISHED')
  with self.assertRaises(AssertionError):c.publish('studio',r['alignment_hash'],0)
 def test_unknown_is_not_permission(self):
  a=self.labels();a[a.index('E')]='U';self.assertFalse(ns['routes'](p,a));self.assertTrue(ns['routes'](p,a,True))
 def test_missing_translation_no_skip(self):
  a=['N']*len(ns['blocks'](p));self.assertFalse(ns['routes'](p,a))
 def test_reverse_alignment_rejected(self):
  a=['E' if e[:2] in [[0,1],[1,0]] else 'N' for e in ns['blocks'](p)];self.assertFalse(ns['routes'](p,a))
 def test_validator_checks_unused_cells(self):
  c=self.contract();a=self.labels();b=a.copy();b[-1]='U' if a[-1]!='U' else 'N';answers.extend([a,b])
  with self.assertRaises(AssertionError):c.align('studio')
  self.assertEqual(json.loads(c.read(sender.sender_address,'studio'))['phase'],'SEALED')
 def test_owner_hash_and_index_guards(self):
  c=self.contract();a=self.labels();answers.extend([a,a]);c.align('studio');r=json.loads(c.read(sender.sender_address,'studio'))
  with self.assertRaises(AssertionError):c.publish('studio','wrong',0)
  with self.assertRaises(AssertionError):c.publish('studio',r['alignment_hash'],-1)
  sender.sender_address='0x'+'2'*40
  with self.assertRaises(KeyError):c.publish('studio',r['alignment_hash'],0)
 def test_invalid_timing_and_markup(self):
  q=json.loads(json.dumps(p));q['source'][1]['start']=100
  with self.assertRaises(AssertionError):ns['check'](json.dumps(q))
  q=json.loads(json.dumps(p));q['target'][0]='<b>九点</b>'
  with self.assertRaises(AssertionError):ns['check'](json.dumps(q))
 def test_finest_complete_paths_only(self):
  q=json.loads(json.dumps(p));q['source']=q['source'][:2];q['target']=['甲','乙'];a=['E']*len(ns['blocks'](q));paths=ns['routes'](q,a);self.assertTrue(all(len(x)==2 for x in paths))
unittest.main()
