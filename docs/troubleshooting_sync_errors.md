---
source: troubleshooting_sync_errors
doc_type: troubleshooting
last_updated: 2026-04-02
access_level: public
---

# Troubleshooting Sync Errors

## Error SYNC-101: Conflict detected
This appears when the same file was edited on two devices while offline.
CloudSync keeps both versions and appends "(conflicted copy)" to the
filename of the older edit. Resolve manually by merging changes.

## Error SYNC-204: Quota exceeded
Returned when the account's storage quota is full. Free tier accounts have
a 5 GB quota. Upgrading the plan or deleting files resolves this.

## Error SYNC-317: Device limit reached
Returned when a user tries to connect a new device after reaching their
plan's device limit (see the General FAQ for current limits per tier).
Removing an existing device from Settings > Devices frees up a slot.

## Sync stuck at "Preparing to sync"
This usually means the local sync database is corrupted. Steps:
1. Pause sync.
2. Delete the local `.cloudsync-db` folder.
3. Resume sync to force a full re-index.

## Files not syncing but no error shown
Check that the folder is not excluded via `.cloudsyncignore`. Also confirm
the device's local clock is correct — sync conflict detection depends on
accurate timestamps.
