# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

with open("res/avatar.png", "rb") as f:
    data = f.read()
    userAvatar = data.encode("base64")

userFixtures = [{'userEmail': 'user@mail.com',
                 'userName': 'John Doe',
                 'userPassword': 'password1',
                 'userSkill': ['Python', 'Communication', 'Leadership'],
                 'userTag': ['DTU', 'Digital Media Engineering', 'Android'],
                 'userAvatar': userAvatar,
                 },
                {'userEmail': 'tester@mail.com',
                 'userName': 'Jane Doe',
                 'userPassword': 'password2',
                 },
                ]
ratingFixtures = [{'userEmail': userFixtures[0]['userEmail'],
                   'ratingUserEmail': userFixtures[1]['userEmail'],
                   'ratingValue': 5,
                   },
                  ]

huddle_timestamp = datetime.now() - datetime.utcfromtimestamp(0)
huddle_timestamp = ('%.0f' % (huddle_timestamp.total_seconds() * 1000))

huddleFixtures = [{'huddleDateAndTime': huddle_timestamp,
                   'huddleLocation': ['55.785061', '12.519927'],
                   'huddleAdmin': userFixtures[0]['userEmail'],
                   'huddleName': 'Mobile Prototyping',
                   'huddleTag': ['DTU', '02728', 'Digital Media Engineering'],
                   'huddleUser': [userFixtures[0]['userEmail'],
                                  userFixtures[1]['userEmail']],
                   },
                  {'huddleDateAndTime': str(int(huddle_timestamp) - 172800000),
                   'huddleLocation': ['56.785061', '11.519927'],
                   'huddleAdmin': userFixtures[0]['userEmail'],
                   'huddleName': 'Agile Digital Media Development',
                   'huddleTag': ['DTU', '02725'],
                   'huddleUser': [userFixtures[0]['userEmail'],
                                  userFixtures[1]['userEmail']],
                   },
                  ]

groupFixtures = [{'huddleName': huddleFixtures[0]['huddleName'],
                  'groupName': 'Group 1',
                  'groupUser': [userFixtures[0]['userEmail'],
                                userFixtures[1]['userEmail']],
                  'groupAdmin': userFixtures[0]['userEmail'],
                  },
                 ]

appointmentFixtures = [{'huddleName': huddleFixtures[0]['huddleName'],
                        'groupName': groupFixtures[0]['groupName'],
                        'appointmentName': 'Hangout',
                        'appointmentTime': datetime(2014, 4, 9, 9, 0, 0),
                        },
                       ]

chatFixtures = [{'huddleName': huddleFixtures[0]['huddleName'],
                 'groupName': groupFixtures[0]['groupName'],
                 'timestamp': datetime(2014, 4, 1, 13, 0, 0),
                 'text': 'Hi!',
                 'author': userFixtures[0]['userEmail'],
                 },
                {'huddleName': huddleFixtures[0]['huddleName'],
                 'groupName': groupFixtures[0]['groupName'],
                 'timestamp': datetime(2014, 4, 1, 13, 0, 10),
                 'text': 'Hello!',
                 'author': userFixtures[1]['userEmail'],
                 },
                {'huddleName': huddleFixtures[0]['huddleName'],
                 'groupName': groupFixtures[0]['groupName'],
                 'timestamp': datetime(2014, 4, 1, 13, 0, 15),
                 'text': 'Whats up?',
                 'author': userFixtures[0]['userEmail'],
                 },
                {'huddleName': huddleFixtures[0]['huddleName'],
                 'groupName': groupFixtures[0]['groupName'],
                 'timestamp': datetime(2014, 4, 1, 13, 0, 25),
                 'text': 'Nothing special',
                 'author': userFixtures[1]['userEmail'],
                 },
                {'huddleName': huddleFixtures[0]['huddleName'],
                 'groupName': groupFixtures[0]['groupName'],
                 'timestamp': datetime(2014, 4, 1, 13, 0, 30),
                 'text': 'Ok, I was just wondering when we can meet next time.',
                 'author': userFixtures[0]['userEmail'],
                 },
                {'huddleName': huddleFixtures[0]['huddleName'],
                 'groupName': groupFixtures[0]['groupName'],
                 'timestamp': datetime(2014, 4, 1, 13, 0, 35),
                 'text': 'Maybe Monday evening?',
                 'author': userFixtures[1]['userEmail'],
                 },
                {'huddleName': huddleFixtures[0]['huddleName'],
                 'groupName': groupFixtures[0]['groupName'],
                 'timestamp': datetime(2014, 4, 1, 13, 0, 40),
                 'text': 'Monday is not good for me, what about Thuesday at 9am?',
                 'author': userFixtures[0]['userEmail'],
                 },
                {'huddleName': huddleFixtures[0]['huddleName'],
                 'groupName': groupFixtures[0]['groupName'],
                 'timestamp': datetime(2014, 4, 1, 13, 0, 45),
                 'text': 'Thuesday sounds good, see you then',
                 'author': userFixtures[1]['userEmail'],
                 },
                {'huddleName': huddleFixtures[0]['huddleName'],
                 'groupName': groupFixtures[0]['groupName'],
                 'timestamp': datetime(2014, 4, 1, 13, 0, 50),
                 'text': 'Cool, see you.',
                 'author': userFixtures[0]['userEmail'],
                 },
                ]
geoFixtures = [{'startLat': 0.,
                'distance': 1000.,
                'dlat': 0.00899068,
                'dlon': 0.00899068}]

huddleDate = datetime.now() - timedelta(days=1)
huddleDate = huddleDate.strftime('%Y-%m-%d')
settingsFixtures = {'userLocation': ['55.7852', '12.5198'],
                    'filterDistance': 100.,
                    'searchTags': huddleFixtures[0]['huddleTag'],
                    'huddleDate': huddleDate,
                    }
