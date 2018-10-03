#!/usr/bin/env python3
#coding: utf-8
#
import json
import paho.mqtt.client as mqtt_client
 
class Temperature(object):
  ACQUIRE_FREQ =30
  client = None

  def __init__(self):
      #MQTT client initialization 
     self.client = mqtt_client.Client()
     self.client.on_connect = self.on_connect
     self.client.on_message = self.on_message
      
     self.client.connect('192.168.0.213',1883,60);
     self.client.loop_start()

def on_connect(self, client, userdata,flags, rc):
    if(rc != 0 ):return
    self.client.subscribe('R1/014/temperature/command');

def sendData(self):
  "'sending temperatures'"

  jsonFrame= dict();
  jsonFrame['unitID'] = '02:00:c0:a8:00:12'|'vm-dyn-0-213.siame.univ-tlse3.fr'
  jsonFrame['temperature'] = '10'

  res, mid = self.client.publish( 'R1/014/temperature/command', json.dumps(jsonFrame))
 
  "'paho callback for message reception'"
def _on_message(self, client, userdata, msg):
    if msg.topic != self._command_topic:
       #this module is not concerned by this message, returning
       log.debug("received a message not for me on" + msg.topic)
    try:
       #loading nd verifiying payload 
       payload = json.load(msg.payload.decode('utf-8'))
    except Exception as ex:
      log.error("exception handling json paload: " + str(ex))
      return
    else:
      # executed if no exception arise
      if payload['dest'] != "all" and payload['dest'] != str(self.unitID):
          return
