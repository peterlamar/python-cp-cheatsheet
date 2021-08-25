import json
import sys



## Conditions

def isInt(s):
  try:
    int(s)
    return True
  except ValueError:
    return False

def getEventVar(event, key):
  e = event
  for k in key.split('.'):
    e = e[k]
  return e

def getLeftRight(event, c, dir):
  if isInt(c[dir]):
    return c[dir]
  elif c[dir] and c[dir][0] == '$':
    key = c[dir][1:]
    return getEventVar(event, key)
  else:
    return c[dir]

def isEqualTo(event, c):
  l = getLeftRight(event, c, 'left')
  r = getLeftRight(event, c, 'right')
  return l == r

def isLessThan(event, c):
  l = getLeftRight(event, c, 'left')
  r = getLeftRight(event, c, 'right')
  return l < r

def isLessThanEqual(event, c):
  l = getLeftRight(event, c, 'left')
  r = getLeftRight(event, c, 'right')
  return l <= r

## Actions

def writeField(event, a):
  if a['keyPath'] and a['keyPath'][0] == '$': 
    key = a['keyPath'][1:]
    if a['overwriteIfExists'] == False:
      if event[key]:
        return
    event[key] = a['value']
  
  return event

## Main

def process_event(event, rules):
  rtn = event
  for r in rules:
    res = []
    for c in r['conditions']['all']:
      if c['operator'] == 'equalTo':
        res.append(isEqualTo(event, c))
      if c['operator'] == 'lessThan':
        res.append(isLessThan(event, c))
      if c['operator'] == 'lessThanEqual':
        res.append(isLessThanEqual(event, c))
    if all(res):
      for a in r['actions']:
        if a['action'] == 'dropEvent':
          return None
        if a['action'] == 'writeField':
          rtn = writeField(event, a)
  return rtn

    

        

# You need to implement this function. Feel free to organize your code into
# whatever other classes and functions you see fit.
def process_events(event_stream, rules):

    # iterate through event stream and pass individual events
    # Succeed if condition applies to event
    rtn = []
    for e in event_stream:
      ep = process_event(e, rules)
      if ep:
        rtn.append(ep)

    # Your return value should be the list of events that results from applying the rules to
    # event_stream. The value returned from the most recent run of your program will be in
    # output.json.
    return rtn


# ***DO NOT EDIT BELOW THIS LINE***

##########
# main
##########


def usage():
    print("processor.py [rules.json] [eventStream.json]")
    exit(1)


if __name__ == "__main__":
    if len(sys.argv) > 3:
        usage()

    # default to these files in cwd
    event_stream_file = "eventStream.json"
    rules_file = "rules.json"

    if len(sys.argv) >= 3:
        event_stream_file = sys.argv[2]
    if len(sys.argv) >= 2:
        rules_file = sys.argv[1]

    event_stream = json.load(open(event_stream_file))
    rules = json.load(open(rules_file))

    processed_events = process_events(event_stream, rules)
    j = json.dumps(processed_events, indent=2)
    with open("output.json", "w") as f:
        f.write(j)
