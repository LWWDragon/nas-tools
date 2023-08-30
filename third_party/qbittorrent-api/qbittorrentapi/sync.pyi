from typing import Text

from qbittorrentapi.app import AppAPIMixIn
from qbittorrentapi.definitions import ClientCache
from qbittorrentapi.definitions import Dictionary

class SyncMainDataDictionary(Dictionary): ...
class SyncTorrentPeersDictionary(Dictionary): ...

class Sync(ClientCache):
    maindata: _MainData
    torrent_peers: _TorrentPeers
    torrentPeers: _TorrentPeers
    def __init__(self, client: SyncAPIMixIn) -> None: ...

    class _MainData(ClientCache):
        _rid: int | None
        def __init__(self, client: SyncAPIMixIn) -> None: ...
        def __call__(
            self, rid: Text | int = None, **kwargs
        ) -> SyncMainDataDictionary: ...
        def delta(self, **kwargs) -> SyncMainDataDictionary: ...
        def reset_rid(self) -> None: ...

    class _TorrentPeers(ClientCache):
        _rid: int | None
        def __init__(self, client: SyncAPIMixIn) -> None: ...
        def __call__(
            self, torrent_hash: Text = None, rid: Text | int = None, **kwargs
        ) -> SyncTorrentPeersDictionary: ...
        def delta(
            self, torrent_hash: Text = None, **kwargs
        ) -> SyncTorrentPeersDictionary: ...
        def reset_rid(self) -> None: ...

class SyncAPIMixIn(AppAPIMixIn):
    @property
    def sync(self) -> Sync: ...
    def sync_maindata(
        self, rid: Text | int = 0, **kwargs
    ) -> SyncMainDataDictionary: ...
    def sync_torrent_peers(
        self, torrent_hash: Text = None, rid: Text | int = 0, **kwargs
    ) -> SyncTorrentPeersDictionary: ...
    sync_torrentPeers = sync_torrent_peers