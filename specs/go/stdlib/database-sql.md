Go Wiki: SQL Database Drivers - The Go Programming Language/[Skip to Main Content](#main-content)

- [Why Go arrow_drop_down](#) Press Enter to activate/deactivate dropdown 

  - [Case Studies](/solutions/case-studies)

Common problems companies solve with Go

  - [Use Cases](/solutions/use-cases)

Stories about how and why companies use Go

  - [Security](/security/)

How Go can help keep you secure by default

- [Learn](/learn/) Press Enter to activate/deactivate dropdown 
- [Docs arrow_drop_down](#) Press Enter to activate/deactivate dropdown 

  - [Go Spec](/ref/spec)

The official Go language specification

  - [Go User Manual](/doc)

A complete introduction to building software with Go

  - [Standard library](https://pkg.go.dev/std)

Reference documentation for Go's standard library

  - [Release Notes](/doc/devel/release)

Learn what's new in each Go release

  - [Effective Go](/doc/effective_go)

Tips for writing clear, performant, and idiomatic Go code

- [Packages](https://pkg.go.dev) Press Enter to activate/deactivate dropdown 
- [Community arrow_drop_down](#) Press Enter to activate/deactivate dropdown 

  - [Recorded Talks](/talks/)

Videos from prior events

  - [Meetups
                           open_in_new](https://www.meetup.com/pro/go)

Meet other local Go developers

  - [Conferences
                           open_in_new](/wiki/Conferences)

Learn and network with Go developers from around the world

  - [Go blog](/blog)

The Go project's official blog.

  - [Go project](/help)

Get help and stay informed from Go

  -  Get connected 

https://groups.google.com/g/golang-nutshttps://github.com/golanghttps://twitter.com/golanghttps://www.reddit.com/r/golang/https://invite.slack.golangbridge.org/https://stackoverflow.com/tags/go

/

- [Why Go navigate_next](#)[navigate_beforeWhy Go](#)

  - [Case Studies](/solutions/case-studies)
  - [Use Cases](/solutions/use-cases)
  - [Security](/security/)

- [Learn](/learn/)
- [Docs navigate_next](#)[navigate_beforeDocs](#)

  - [Go Spec](/ref/spec)
  - [Go User Manual](/doc)
  - [Standard library](https://pkg.go.dev/std)
  - [Release Notes](/doc/devel/release)
  - [Effective Go](/doc/effective_go)

- [Packages](https://pkg.go.dev)
- [Community navigate_next](#)[navigate_beforeCommunity](#)

  - [Recorded Talks](/talks/)
  - [Meetups
                           open_in_new](https://www.meetup.com/pro/go)
  - [Conferences
                           open_in_new](/wiki/Conferences)
  - [Go blog](/blog)
  - [Go project](/help)
  - Get connectedhttps://groups.google.com/g/golang-nutshttps://github.com/golanghttps://twitter.com/golanghttps://www.reddit.com/r/golang/https://invite.slack.golangbridge.org/https://stackoverflow.com/tags/go

# Go Wiki: SQL Database Drivers

The database/sql and database/sql/driver packages are designed for using databases from Go and implementing database drivers, respectively.

See the design goals doc:

[http://golang.org/src/pkg/database/sql/doc.txt](http://golang.org/src/pkg/database/sql/doc.txt)

## Drivers

Drivers for Go’s sql package include:

- Amazon AWS Athena: [https://github.com/uber/athenadriver](https://github.com/uber/athenadriver)
- AWS Athena: [https://github.com/segmentio/go-athena](https://github.com/segmentio/go-athena)
- AWS DynamoDB: [https://github.com/btnguyen2k/godynamo](https://github.com/btnguyen2k/godynamo)
- Apache Avatica/Phoenix: [https://github.com/apache/calcite-avatica-go](https://github.com/apache/calcite-avatica-go)
- Apache H2: [https://github.com/jmrobles/h2go](https://github.com/jmrobles/h2go)
- Apache Hive: [https://github.com/sql-machine-learning/gohive](https://github.com/sql-machine-learning/gohive)
- Apache Ignite/GridGain: [https://github.com/amsokol/ignite-go-client](https://github.com/amsokol/ignite-go-client)
- Apache Impala: [https://github.com/bippio/go-impala](https://github.com/bippio/go-impala)
- Azure Cosmos DB: [https://github.com/btnguyen2k/gocosmos](https://github.com/btnguyen2k/gocosmos)
- ClickHouse (uses [HTTP API](https://clickhouse.tech/docs/en/interfaces/http/)): [https://github.com/mailru/go-clickhouse](https://github.com/mailru/go-clickhouse)
- ClickHouse (uses [native TCP interface](https://clickhouse.tech/docs/en/interfaces/tcp/)): [https://github.com/ClickHouse/clickhouse-go](https://github.com/ClickHouse/clickhouse-go)
- CockroachDB: Use any PostgreSQL driver
- Couchbase N1QL: [https://github.com/couchbase/go_n1ql](https://github.com/couchbase/go_n1ql)
- DB2 LUW (uses cgo): [https://github.com/asifjalil/cli](https://github.com/asifjalil/cli)
- DB2 LUW and DB2/Z with DB2-Connect: [https://bitbucket.org/phiggins/db2cli](https://bitbucket.org/phiggins/db2cli) (Last updated 2015-08)
- DB2 LUW, z/OS, iSeries and Informix: [https://github.com/ibmdb/go_ibm_db](https://github.com/ibmdb/go_ibm_db)
- Databricks: [https://github.com/databricks/databricks-sql-go](https://github.com/databricks/databricks-sql-go)
- DuckDB: [https://github.com/marcboeker/go-duckdb](https://github.com/marcboeker/go-duckdb)
- Exasol: (pure Go): [https://github.com/exasol/exasol-driver-go](https://github.com/exasol/exasol-driver-go)
- Firebird SQL: [https://github.com/nakagami/firebirdsql](https://github.com/nakagami/firebirdsql)
- Genji (pure go): [https://github.com/genjidb/genji](https://github.com/genjidb/genji)
- Google Cloud BigQuery: [https://github.com/solcates/go-sql-bigquery](https://github.com/solcates/go-sql-bigquery)
- Google Cloud Spanner: [https://github.com/googleapis/go-sql-spanner](https://github.com/googleapis/go-sql-spanner)
- Google Cloud Spanner: [https://github.com/rakyll/go-sql-driver-spanner](https://github.com/rakyll/go-sql-driver-spanner)
- MS ADODB: [https://github.com/mattn/go-adodb](https://github.com/mattn/go-adodb)
- MS SQL Server (pure go): [https://github.com/microsoft/go-mssqldb](https://github.com/microsoft/go-mssqldb)
- MS SQL Server (uses cgo): [https://github.com/minus5/gofreetds](https://github.com/minus5/gofreetds)
- MaxCompute: [https://github.com/sql-machine-learning/gomaxcompute](https://github.com/sql-machine-learning/gomaxcompute)
- MySQL: [https://github.com/go-sql-driver/mysql/](https://github.com/go-sql-driver/mysql/)`[*]`
- MySQL: [https://github.com/go-mysql-org/go-mysql](https://github.com/go-mysql-org/go-mysql)`[**]` (also handles replication)
- MySQL: [https://github.com/ziutek/mymysql](https://github.com/ziutek/mymysql)`[*]`
- ODBC: [https://bitbucket.org/miquella/mgodbc](https://bitbucket.org/miquella/mgodbc) (Last updated 2016-02)
- ODBC: [https://github.com/alexbrainman/odbc](https://github.com/alexbrainman/odbc)
- Oracle (pure go): [https://github.com/sijms/go-ora](https://github.com/sijms/go-ora)
- Oracle (uses cgo): [https://github.com/godror/godror](https://github.com/godror/godror)
- Oracle (uses cgo): [https://github.com/mattn/go-oci8](https://github.com/mattn/go-oci8)
- Oracle (uses cgo): [https://gopkg.in/rana/ora.v4](https://gopkg.in/rana/ora.v4)
- Postgres (pure Go): [https://github.com/jackc/pgx](https://github.com/jackc/pgx)`[*]`
- Postgres (pure Go): [https://github.com/lib/pq](https://github.com/lib/pq)`[*]`
- Postgres (uses cgo): [https://github.com/jbarham/gopgsqldriver](https://github.com/jbarham/gopgsqldriver)
- Presto: [https://github.com/prestodb/presto-go-client](https://github.com/prestodb/presto-go-client)
- QL: [https://pkg.go.dev/modernc.org/ql](https://pkg.go.dev/modernc.org/ql)
- SAP ASE (pure go): [https://github.com/SAP/go-ase](https://github.com/SAP/go-ase)
- SAP ASE (uses cgo): [https://github.com/SAP/cgo-ase](https://github.com/SAP/cgo-ase)
- SAP HANA (pure go): [https://github.com/SAP/go-hdb](https://github.com/SAP/go-hdb)
- SAP HANA (uses cgo): [https://help.sap.com/viewer/0eec0d68141541d1b07893a39944924e/2.0.03/en-US/0ffbe86c9d9f44338441829c6bee15e6.html](https://help.sap.com/viewer/0eec0d68141541d1b07893a39944924e/2.0.03/en-US/0ffbe86c9d9f44338441829c6bee15e6.html)
- SQL over REST: [https://github.com/adaptant-labs/go-sql-rest-driver](https://github.com/adaptant-labs/go-sql-rest-driver)
- SQLite (uses cgo): [https://github.com/gwenn/gosqlite](https://github.com/gwenn/gosqlite) - Supports SQLite dynamic data typing
- SQLite (uses cgo): [https://github.com/mattn/go-sqlite3](https://github.com/mattn/go-sqlite3)`[*]`
- SQLite (uses cgo): [https://github.com/mxk/go-sqlite](https://github.com/mxk/go-sqlite)
- SQLite: (pure go): [https://modernc.org/sqlite](https://modernc.org/sqlite)
- SQLite: (pure go): [https://github.com/ncruces/go-sqlite3](https://github.com/ncruces/go-sqlite3)
- SQLite: (uses cgo): [https://github.com/rsc/sqlite](https://github.com/rsc/sqlite)
- SingleStore: Use any MySQL driver
- Snowflake (pure Go): [https://github.com/snowflakedb/gosnowflake](https://github.com/snowflakedb/gosnowflake)
- Sybase ASE (pure go): [https://github.com/thda/tds](https://github.com/thda/tds)
- Sybase SQL Anywhere: [https://github.com/a-palchikov/sqlago](https://github.com/a-palchikov/sqlago)
- TiDB: Use any MySQL driver
- Trino: [https://github.com/trinodb/trino-go-client](https://github.com/trinodb/trino-go-client)
- Vertica: [https://github.com/vertica/vertica-sql-go](https://github.com/vertica/vertica-sql-go)
- Vitess: [https://pkg.go.dev/vitess.io/vitess/go/vt/vitessdriver](https://pkg.go.dev/vitess.io/vitess/go/vt/vitessdriver)
- YDB (pure go): [https://github.com/ydb-platform/ydb-go-sdk](https://github.com/ydb-platform/ydb-go-sdk)
- YQL (Yahoo! Query Language): [https://github.com/mattn/go-yql](https://github.com/mattn/go-yql)

Drivers marked with `[*]` are both included in and pass the compatibility test suite at [https://github.com/bradfitz/go-sql-test](https://github.com/bradfitz/go-sql-test). Drivers marked with `[**]` pass the compatibility test suite but are not currently included in it.

This content is part of the [Go Wiki](/wiki/).

[Why Go](/solutions/)[Use Cases](/solutions/use-cases)[Case Studies](/solutions/case-studies)[Get Started](/learn/)[Playground](/play)[Tour](/tour/)[Stack Overflow](https://stackoverflow.com/questions/tagged/go?tab=Newest)[Help](/help/)[Packages](https://pkg.go.dev)[Standard Library](/pkg/)[About Go Packages](https://pkg.go.dev/about)[About](/project)[Download](/dl/)[Blog](/blog/)[Issue Tracker](https://github.com/golang/go/issues)[Release Notes](/doc/devel/release)[Brand Guidelines](/brand)[Code of Conduct](/conduct)[Connect](https://www.twitter.com/golang)[Twitter](https://www.twitter.com/golang)[GitHub](https://github.com/golang)[Slack](https://invite.slack.golangbridge.org/)[r/golang](https://reddit.com/r/golang)[Meetup](https://www.meetup.com/pro/go)[Golang Weekly](https://golangweekly.com/) Opens in new window. 

- [Copyright](/copyright)
- [Terms of Service](/tos)
- [Privacy Policy](http://www.google.com/intl/en/policies/privacy/)
- [Report an Issue](/s/website-issue)
- 

https://google.comgo.dev uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)Okay
