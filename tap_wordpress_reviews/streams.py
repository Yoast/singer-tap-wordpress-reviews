"""Streams."""
# -*- coding: utf-8 -*-

from types import MappingProxyType

# Streams metadata
STREAMS: MappingProxyType = MappingProxyType({
    'reviews': {
        'key_properties': 'path',
        'replication_method': 'INCREMENTAL',
        'replication_key': 'path',
        'bookmark': 'date',
    },
})
