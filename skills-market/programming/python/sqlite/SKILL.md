---
name: SQLite
domain: programming
description: Design or repair SQLite transactions, concurrency, schema changes, query plans or backups. Use for SQLite-specific behavior and integrity questions; not a blanket migration recommendation for every web application.
metadata:
  version: "1.0.1"
  clawdbot:
    emoji: 🪶
    requires:
      bins:
      - sqlite3
    os:
    - linux
    - darwin
    - win32
---

# SQLite Integrity and Concurrency

Inspect the linked SQLite version, journal mode, connection/transaction settings
and workload before changing pragmas. SQLite permits many readers but one writer
at a time; suitability depends on write duration/contention, not merely having
multiple users. A busy timeout helps bounded contention but does not fix long
transactions or remove SQLITE_BUSY handling.

- In WAL mode, readers can coexist with a writer. `BEGIN IMMEDIATE` acquires a
  write transaction early; it can still fail when another writer is active.
  `BEGIN EXCLUSIVE` and IMMEDIATE behave the same in WAL; outside WAL, EXCLUSIVE
  also prevents other connections reading during that transaction.
- Enable/check `PRAGMA foreign_keys` on every relevant connection before relying
  on constraints; configure outside an active transaction. Preserve connection
  ownership and use savepoints for nested rollback scopes.
- Type affinity is not a validation contract. Check actual version/STRICT support;
  model booleans, timestamps/timezones and floating-point precision explicitly.
- Schema rebuilds need preserved indexes, triggers, foreign keys and data, with
  a transaction/migration test appropriate to the change. Confirm the installed
  ALTER TABLE capabilities rather than assuming an old feature list.
- Use bound parameters for data values. Query plans and representative timings
  should justify indexes/pragmas; durability settings change failure behavior.

## Backups and maintenance

Use the online backup API, shell `.backup`, or supported `VACUUM INTO` for a
consistent standalone copy. Do not copy a live database and its WAL/SHM files in
separate filesystem operations and call that an atomic backup. Verify a backup
can be opened and contains the expected data before replacing a source.

VACUUM rewrites the database and needs time, space and suitable locking. It is
optional maintenance when space reclamation or another concrete goal warrants it,
not mandatory after every bulk delete. Preserve explicit primary keys rather than
assuming anonymous ROWIDs remain stable across rewrites. `:memory:` normally names
a separate database per connection; a shared URI has connection-lifetime constraints.

Stop when the scoped query, transaction, migration or backup is verified. References:
[transactions](https://sqlite.org/lang_transaction.html), [backup API](https://sqlite.org/backup.html).
