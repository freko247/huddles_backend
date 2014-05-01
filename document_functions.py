# -*- coding: utf-8 -*-
import logging

from google.appengine.api import search


def createHuddleGeoDoc(huddleData):
    huddleGeoDoc = search.Document(
        fields=[
            search.TextField(name='huddleName',
                             value=huddleData['huddleName']),
            search.GeoField(
                name='huddleLocation',
                value=search.GeoPoint(
                    float(huddleData['huddleLocation'][0]),
                    float(huddleData['huddleLocation'][1]),)),
        ])
    try:
        index = search.Index(name="huddleGeoIndex")
        results = index.put(huddleGeoDoc)
        return results[0].id
    except search.Error:
        logging.exception('Put failed')
        return


def getHuddlesInRange(settingsData):
    index = search.Index(name="huddleGeoIndex")
    query_string = "distance(huddleLocation, geopoint(%s)) < %s" % (
        ','.join(settingsData['userLocation']),
        str(settingsData['filterDistance']),)
    query = search.Query(query_string=query_string)
    huddles = []
    try:
        logging.debug('Executing document search')
        results = index.search(query)
        logging.debug('Found %s matching documents' % len(results.results))
        for scored_document in results:
            logging.debug('Huddle, named %s, is in range.' %
                          scored_document.field('huddleName').value)
            huddles.append(scored_document.field('huddleName').value)
        return huddles
    except search.Error:
        logging.exception('Search failed')
