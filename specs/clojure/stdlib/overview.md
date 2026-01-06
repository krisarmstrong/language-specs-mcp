Overview - Clojure v1.12.4 API documentationindex.html

# [Clojure Core API Reference](index.html)

Clojurev1.12.4 API

- [Overview](index.html)
- [API Index](api-index.html)

Namespaces

- [clojure.core](clojure.core-api.html)
- [clojure.data](clojure.data-api.html)
- [clojure.datafy](clojure.datafy-api.html)
- [clojure.edn](clojure.edn-api.html)
- [clojure.inspector](clojure.inspector-api.html)
- [clojure.instant](clojure.instant-api.html)
- [clojure.java.basis](clojure.java.basis-api.html)
- [clojure.java.browse](clojure.java.browse-api.html)
- [clojure.java.io](clojure.java.io-api.html)
- [clojure.java.javadoc](clojure.java.javadoc-api.html)
- [clojure.java.process](clojure.java.process-api.html)
- [clojure.java.shell](clojure.java.shell-api.html)
- [clojure.main](clojure.main-api.html)
- [clojure.math](clojure.math-api.html)
- [clojure.pprint](clojure.pprint-api.html)
- [clojure.reflect](clojure.reflect-api.html)
- [clojure.repl](clojure.repl-api.html)
- [clojure.set](clojure.set-api.html)
- [clojure.stacktrace](clojure.stacktrace-api.html)
- [clojure.string](clojure.string-api.html)
- [clojure.template](clojure.template-api.html)
- [clojure.test](clojure.test-api.html)
- [clojure.tools.deps.interop](clojure.tools.deps.interop-api.html)
- [clojure.walk](clojure.walk-api.html)
- [clojure.xml](clojure.xml-api.html)
- [clojure.zip](clojure.zip-api.html)

Other Versions

- [v1.12.3 (stable)](index.html)
- [v1.13 (in development)](branch-master/index.html)
- [v1.11.4 (legacy)](branch-clojure-1.11.4/index.html)
- [v1.10.3 (legacy)](branch-clojure-1.10.3/index.html)
- [v1.9 (legacy)](branch-clojure-1.9.0/index.html)
- [v1.8 (legacy)](branch-clojure-1.8.0/index.html)
- [v1.7 (legacy)](branch-clojure-1.7.0/index.html)
- [v1.6 (legacy)](branch-clojure-1.6.0/index.html)
- [v1.5 (legacy)](branch-clojure-1.5.0/index.html)
- [v1.4 (legacy)](branch-clojure-1.4.0/index.html)
- [v1.3 (legacy)](branch-1.3.x/index.html)
- [v1.2 (legacy)](branch-1.2.x/index.html)
- [v1.1 (legacy)](branch-1.1.x/index.html)

[Clojure Home](https://clojure.org)

# Table of Contents

[clojure.core](#clojure.core)[clojure.data](#clojure.data)[clojure.datafy](#clojure.datafy)[clojure.edn](#clojure.edn)[clojure.inspector](#clojure.inspector)[clojure.instant](#clojure.instant)[clojure.java.basis](#clojure.java.basis)[clojure.java.browse](#clojure.java.browse)[clojure.java.io](#clojure.java.io)[clojure.java.javadoc](#clojure.java.javadoc)[clojure.java.process](#clojure.java.process)[clojure.java.shell](#clojure.java.shell)[clojure.main](#clojure.main)[clojure.math](#clojure.math)[clojure.pprint](#clojure.pprint)[clojure.reflect](#clojure.reflect)[clojure.repl](#clojure.repl)[clojure.set](#clojure.set)[clojure.stacktrace](#clojure.stacktrace)[clojure.string](#clojure.string)[clojure.template](#clojure.template)[clojure.test](#clojure.test)[clojure.tools.deps.interop](#clojure.tools.deps.interop)[clojure.walk](#clojure.walk)[clojure.xml](#clojure.xml)[clojure.zip](#clojure.zip)

# API Overview - Clojurev1.12.4 (stable)

### Important Clojure resources

- The official source code for clojure is on the [Clojure GitHub source page](https://github.com/clojure/clojure/). 
- Clojure provides a Java API for invoking Clojure from Java. You can browse the javadoc for the API at [https://clojure.github.io/clojure/javadoc](https://clojure.github.io/clojure/javadoc). 
- Issues related to Clojure and the various pieces of functionality within it are discussed in the [Clojure Google group](https://groups.google.com/group/clojure). 
- Discussions among Clojure developers take place in the [Clojure Dev Google group](https://groups.google.com/group/clojure-dev). 
- Development planning, design, and documentation happen in [the Confluence Clojure space](https://dev.clojure.org). 
- Issue tracking happens on the [the Clojure JIRA site](https://dev.clojure.org/jira/browse/CLJ). 
- This documentation is maintained in the gh-pages branch of Clojure on GitHub and is always available online [GitHub pages for Clojure](https://clojure.github.io/clojure). If you wish to have a version for off-line use you can use the download button on the [gh-pages branch page at GitHub](https://github.com/clojure/clojure/tree/gh-pages). 

## clojure.core

[Detailed API documentation](clojure.core-api.html)

```
Fundamental library of the Clojure language
```

 Contents: [&](clojure.core-api.html#clojure.core/&)[*](clojure.core-api.html#clojure.core/*)[*'](clojure.core-api.html#clojure.core/*')[*1](clojure.core-api.html#clojure.core/*1)[*2](clojure.core-api.html#clojure.core/*2)[*3](clojure.core-api.html#clojure.core/*3)[*agent*](clojure.core-api.html#clojure.core/*agent*)[*assert*](clojure.core-api.html#clojure.core/*assert*)[*clojure-version*](clojure.core-api.html#clojure.core/*clojure-version*)[*command-line-args*](clojure.core-api.html#clojure.core/*command-line-args*)[*compile-files*](clojure.core-api.html#clojure.core/*compile-files*)[*compile-path*](clojure.core-api.html#clojure.core/*compile-path*)[*compiler-options*](clojure.core-api.html#clojure.core/*compiler-options*)[*data-readers*](clojure.core-api.html#clojure.core/*data-readers*)[*default-data-reader-fn*](clojure.core-api.html#clojure.core/*default-data-reader-fn*)[*e](clojure.core-api.html#clojure.core/*e)[*err*](clojure.core-api.html#clojure.core/*err*)[*file*](clojure.core-api.html#clojure.core/*file*)[*flush-on-newline*](clojure.core-api.html#clojure.core/*flush-on-newline*)[*in*](clojure.core-api.html#clojure.core/*in*)[*ns*](clojure.core-api.html#clojure.core/*ns*)[*out*](clojure.core-api.html#clojure.core/*out*)[*print-dup*](clojure.core-api.html#clojure.core/*print-dup*)[*print-length*](clojure.core-api.html#clojure.core/*print-length*)[*print-level*](clojure.core-api.html#clojure.core/*print-level*)[*print-meta*](clojure.core-api.html#clojure.core/*print-meta*)[*print-namespace-maps*](clojure.core-api.html#clojure.core/*print-namespace-maps*)[*print-readably*](clojure.core-api.html#clojure.core/*print-readably*)[*read-eval*](clojure.core-api.html#clojure.core/*read-eval*)[*repl*](clojure.core-api.html#clojure.core/*repl*)[*unchecked-math*](clojure.core-api.html#clojure.core/*unchecked-math*)[*warn-on-reflection*](clojure.core-api.html#clojure.core/*warn-on-reflection*)[+](clojure.core-api.html#clojure.core/+)[+'](clojure.core-api.html#clojure.core/+')[-](clojure.core-api.html#clojure.core/-)[-'](clojure.core-api.html#clojure.core/-')[->](clojure.core-api.html#clojure.core/->)[->>](clojure.core-api.html#clojure.core/->>)[->ArrayChunk](clojure.core-api.html#clojure.core/->ArrayChunk)[->Eduction](clojure.core-api.html#clojure.core/->Eduction)[->Vec](clojure.core-api.html#clojure.core/->Vec)[->VecNode](clojure.core-api.html#clojure.core/->VecNode)[->VecSeq](clojure.core-api.html#clojure.core/->VecSeq)[.](clojure.core-api.html#clojure.core/.)[..](clojure.core-api.html#clojure.core/..)[/](clojure.core-api.html#clojure.core//)[<](clojure.core-api.html#clojure.core/<)[<=](clojure.core-api.html#clojure.core/<=)[=](clojure.core-api.html#clojure.core/=)[==](clojure.core-api.html#clojure.core/==)[>](clojure.core-api.html#clojure.core/>)[>=](clojure.core-api.html#clojure.core/>=)[abs](clojure.core-api.html#clojure.core/abs)[accessor](clojure.core-api.html#clojure.core/accessor)[aclone](clojure.core-api.html#clojure.core/aclone)[add-classpath](clojure.core-api.html#clojure.core/add-classpath)[add-tap](clojure.core-api.html#clojure.core/add-tap)[add-watch](clojure.core-api.html#clojure.core/add-watch)[agent](clojure.core-api.html#clojure.core/agent)[agent-error](clojure.core-api.html#clojure.core/agent-error)[agent-errors](clojure.core-api.html#clojure.core/agent-errors)[aget](clojure.core-api.html#clojure.core/aget)[alength](clojure.core-api.html#clojure.core/alength)[alias](clojure.core-api.html#clojure.core/alias)[all-ns](clojure.core-api.html#clojure.core/all-ns)[alter](clojure.core-api.html#clojure.core/alter)[alter-meta!](clojure.core-api.html#clojure.core/alter-meta!)[alter-var-root](clojure.core-api.html#clojure.core/alter-var-root)[amap](clojure.core-api.html#clojure.core/amap)[ancestors](clojure.core-api.html#clojure.core/ancestors)[and](clojure.core-api.html#clojure.core/and)[any?](clojure.core-api.html#clojure.core/any?)[apply](clojure.core-api.html#clojure.core/apply)[areduce](clojure.core-api.html#clojure.core/areduce)[array-map](clojure.core-api.html#clojure.core/array-map)[ArrayChunk](clojure.core-api.html#clojure.core/ArrayChunk)[as->](clojure.core-api.html#clojure.core/as->)[aset](clojure.core-api.html#clojure.core/aset)[aset-boolean](clojure.core-api.html#clojure.core/aset-boolean)[aset-byte](clojure.core-api.html#clojure.core/aset-byte)[aset-char](clojure.core-api.html#clojure.core/aset-char)[aset-double](clojure.core-api.html#clojure.core/aset-double)[aset-float](clojure.core-api.html#clojure.core/aset-float)[aset-int](clojure.core-api.html#clojure.core/aset-int)[aset-long](clojure.core-api.html#clojure.core/aset-long)[aset-short](clojure.core-api.html#clojure.core/aset-short)[assert](clojure.core-api.html#clojure.core/assert)[assoc](clojure.core-api.html#clojure.core/assoc)[assoc!](clojure.core-api.html#clojure.core/assoc!)[assoc-in](clojure.core-api.html#clojure.core/assoc-in)[associative?](clojure.core-api.html#clojure.core/associative?)[atom](clojure.core-api.html#clojure.core/atom)[await](clojure.core-api.html#clojure.core/await)[await-for](clojure.core-api.html#clojure.core/await-for)[bases](clojure.core-api.html#clojure.core/bases)[bean](clojure.core-api.html#clojure.core/bean)[bigdec](clojure.core-api.html#clojure.core/bigdec)[bigint](clojure.core-api.html#clojure.core/bigint)[biginteger](clojure.core-api.html#clojure.core/biginteger)[binding](clojure.core-api.html#clojure.core/binding)[bit-and](clojure.core-api.html#clojure.core/bit-and)[bit-and-not](clojure.core-api.html#clojure.core/bit-and-not)[bit-clear](clojure.core-api.html#clojure.core/bit-clear)[bit-flip](clojure.core-api.html#clojure.core/bit-flip)[bit-not](clojure.core-api.html#clojure.core/bit-not)[bit-or](clojure.core-api.html#clojure.core/bit-or)[bit-set](clojure.core-api.html#clojure.core/bit-set)[bit-shift-left](clojure.core-api.html#clojure.core/bit-shift-left)[bit-shift-right](clojure.core-api.html#clojure.core/bit-shift-right)[bit-test](clojure.core-api.html#clojure.core/bit-test)[bit-xor](clojure.core-api.html#clojure.core/bit-xor)[boolean](clojure.core-api.html#clojure.core/boolean)[boolean-array](clojure.core-api.html#clojure.core/boolean-array)[boolean?](clojure.core-api.html#clojure.core/boolean?)[booleans](clojure.core-api.html#clojure.core/booleans)[bound-fn](clojure.core-api.html#clojure.core/bound-fn)[bound-fn*](clojure.core-api.html#clojure.core/bound-fn*)[bound?](clojure.core-api.html#clojure.core/bound?)[bounded-count](clojure.core-api.html#clojure.core/bounded-count)[butlast](clojure.core-api.html#clojure.core/butlast)[byte](clojure.core-api.html#clojure.core/byte)[byte-array](clojure.core-api.html#clojure.core/byte-array)[bytes](clojure.core-api.html#clojure.core/bytes)[bytes?](clojure.core-api.html#clojure.core/bytes?)[case](clojure.core-api.html#clojure.core/case)[cast](clojure.core-api.html#clojure.core/cast)[cat](clojure.core-api.html#clojure.core/cat)[catch](clojure.core-api.html#clojure.core/catch)[char](clojure.core-api.html#clojure.core/char)[char-array](clojure.core-api.html#clojure.core/char-array)[char-escape-string](clojure.core-api.html#clojure.core/char-escape-string)[char-name-string](clojure.core-api.html#clojure.core/char-name-string)[char?](clojure.core-api.html#clojure.core/char?)[chars](clojure.core-api.html#clojure.core/chars)[class](clojure.core-api.html#clojure.core/class)[class?](clojure.core-api.html#clojure.core/class?)[clear-agent-errors](clojure.core-api.html#clojure.core/clear-agent-errors)[clojure-version](clojure.core-api.html#clojure.core/clojure-version)[coll?](clojure.core-api.html#clojure.core/coll?)[comment](clojure.core-api.html#clojure.core/comment)[commute](clojure.core-api.html#clojure.core/commute)[comp](clojure.core-api.html#clojure.core/comp)[comparator](clojure.core-api.html#clojure.core/comparator)[compare](clojure.core-api.html#clojure.core/compare)[compare-and-set!](clojure.core-api.html#clojure.core/compare-and-set!)[compile](clojure.core-api.html#clojure.core/compile)[complement](clojure.core-api.html#clojure.core/complement)[completing](clojure.core-api.html#clojure.core/completing)[concat](clojure.core-api.html#clojure.core/concat)[cond](clojure.core-api.html#clojure.core/cond)[cond->](clojure.core-api.html#clojure.core/cond->)[cond->>](clojure.core-api.html#clojure.core/cond->>)[condp](clojure.core-api.html#clojure.core/condp)[conj](clojure.core-api.html#clojure.core/conj)[conj!](clojure.core-api.html#clojure.core/conj!)[cons](clojure.core-api.html#clojure.core/cons)[constantly](clojure.core-api.html#clojure.core/constantly)[construct-proxy](clojure.core-api.html#clojure.core/construct-proxy)[contains?](clojure.core-api.html#clojure.core/contains?)[count](clojure.core-api.html#clojure.core/count)[counted?](clojure.core-api.html#clojure.core/counted?)[create-ns](clojure.core-api.html#clojure.core/create-ns)[create-struct](clojure.core-api.html#clojure.core/create-struct)[cycle](clojure.core-api.html#clojure.core/cycle)[dec](clojure.core-api.html#clojure.core/dec)[dec'](clojure.core-api.html#clojure.core/dec')[decimal?](clojure.core-api.html#clojure.core/decimal?)[declare](clojure.core-api.html#clojure.core/declare)[dedupe](clojure.core-api.html#clojure.core/dedupe)[def](clojure.core-api.html#clojure.core/def)[default-data-readers](clojure.core-api.html#clojure.core/default-data-readers)[definline](clojure.core-api.html#clojure.core/definline)[definterface](clojure.core-api.html#clojure.core/definterface)[defmacro](clojure.core-api.html#clojure.core/defmacro)[defmethod](clojure.core-api.html#clojure.core/defmethod)[defmulti](clojure.core-api.html#clojure.core/defmulti)[defn](clojure.core-api.html#clojure.core/defn)[defn-](clojure.core-api.html#clojure.core/defn-)[defonce](clojure.core-api.html#clojure.core/defonce)[defprotocol](clojure.core-api.html#clojure.core/defprotocol)[defrecord](clojure.core-api.html#clojure.core/defrecord)[defstruct](clojure.core-api.html#clojure.core/defstruct)[deftype](clojure.core-api.html#clojure.core/deftype)[delay](clojure.core-api.html#clojure.core/delay)[delay?](clojure.core-api.html#clojure.core/delay?)[deliver](clojure.core-api.html#clojure.core/deliver)[denominator](clojure.core-api.html#clojure.core/denominator)[deref](clojure.core-api.html#clojure.core/deref)[derive](clojure.core-api.html#clojure.core/derive)[descendants](clojure.core-api.html#clojure.core/descendants)[disj](clojure.core-api.html#clojure.core/disj)[disj!](clojure.core-api.html#clojure.core/disj!)[dissoc](clojure.core-api.html#clojure.core/dissoc)[dissoc!](clojure.core-api.html#clojure.core/dissoc!)[distinct](clojure.core-api.html#clojure.core/distinct)[distinct?](clojure.core-api.html#clojure.core/distinct?)[do](clojure.core-api.html#clojure.core/do)[doall](clojure.core-api.html#clojure.core/doall)[dorun](clojure.core-api.html#clojure.core/dorun)[doseq](clojure.core-api.html#clojure.core/doseq)[dosync](clojure.core-api.html#clojure.core/dosync)[dotimes](clojure.core-api.html#clojure.core/dotimes)[doto](clojure.core-api.html#clojure.core/doto)[double](clojure.core-api.html#clojure.core/double)[double-array](clojure.core-api.html#clojure.core/double-array)[double?](clojure.core-api.html#clojure.core/double?)[doubles](clojure.core-api.html#clojure.core/doubles)[drop](clojure.core-api.html#clojure.core/drop)[drop-last](clojure.core-api.html#clojure.core/drop-last)[drop-while](clojure.core-api.html#clojure.core/drop-while)[eduction](clojure.core-api.html#clojure.core/eduction)[Eduction](clojure.core-api.html#clojure.core/Eduction)[empty](clojure.core-api.html#clojure.core/empty)[empty?](clojure.core-api.html#clojure.core/empty?)[ensure](clojure.core-api.html#clojure.core/ensure)[ensure-reduced](clojure.core-api.html#clojure.core/ensure-reduced)[enumeration-seq](clojure.core-api.html#clojure.core/enumeration-seq)[error-handler](clojure.core-api.html#clojure.core/error-handler)[error-mode](clojure.core-api.html#clojure.core/error-mode)[eval](clojure.core-api.html#clojure.core/eval)[even?](clojure.core-api.html#clojure.core/even?)[every-pred](clojure.core-api.html#clojure.core/every-pred)[every?](clojure.core-api.html#clojure.core/every?)[ex-cause](clojure.core-api.html#clojure.core/ex-cause)[ex-data](clojure.core-api.html#clojure.core/ex-data)[ex-info](clojure.core-api.html#clojure.core/ex-info)[ex-message](clojure.core-api.html#clojure.core/ex-message)[extend](clojure.core-api.html#clojure.core/extend)[extend-protocol](clojure.core-api.html#clojure.core/extend-protocol)[extend-type](clojure.core-api.html#clojure.core/extend-type)[extenders](clojure.core-api.html#clojure.core/extenders)[extends?](clojure.core-api.html#clojure.core/extends?)[false?](clojure.core-api.html#clojure.core/false?)[ffirst](clojure.core-api.html#clojure.core/ffirst)[file-seq](clojure.core-api.html#clojure.core/file-seq)[filter](clojure.core-api.html#clojure.core/filter)[filterv](clojure.core-api.html#clojure.core/filterv)[finally](clojure.core-api.html#clojure.core/finally)[find](clojure.core-api.html#clojure.core/find)[find-keyword](clojure.core-api.html#clojure.core/find-keyword)[find-ns](clojure.core-api.html#clojure.core/find-ns)[find-var](clojure.core-api.html#clojure.core/find-var)[first](clojure.core-api.html#clojure.core/first)[flatten](clojure.core-api.html#clojure.core/flatten)[float](clojure.core-api.html#clojure.core/float)[float-array](clojure.core-api.html#clojure.core/float-array)[float?](clojure.core-api.html#clojure.core/float?)[floats](clojure.core-api.html#clojure.core/floats)[flush](clojure.core-api.html#clojure.core/flush)[fn](clojure.core-api.html#clojure.core/fn)[fn?](clojure.core-api.html#clojure.core/fn?)[fnext](clojure.core-api.html#clojure.core/fnext)[fnil](clojure.core-api.html#clojure.core/fnil)[for](clojure.core-api.html#clojure.core/for)[force](clojure.core-api.html#clojure.core/force)[format](clojure.core-api.html#clojure.core/format)[frequencies](clojure.core-api.html#clojure.core/frequencies)[future](clojure.core-api.html#clojure.core/future)[future-call](clojure.core-api.html#clojure.core/future-call)[future-cancel](clojure.core-api.html#clojure.core/future-cancel)[future-cancelled?](clojure.core-api.html#clojure.core/future-cancelled?)[future-done?](clojure.core-api.html#clojure.core/future-done?)[future?](clojure.core-api.html#clojure.core/future?)[gen-class](clojure.core-api.html#clojure.core/gen-class)[gen-interface](clojure.core-api.html#clojure.core/gen-interface)[gensym](clojure.core-api.html#clojure.core/gensym)[get](clojure.core-api.html#clojure.core/get)[get-in](clojure.core-api.html#clojure.core/get-in)[get-method](clojure.core-api.html#clojure.core/get-method)[get-proxy-class](clojure.core-api.html#clojure.core/get-proxy-class)[get-thread-bindings](clojure.core-api.html#clojure.core/get-thread-bindings)[get-validator](clojure.core-api.html#clojure.core/get-validator)[group-by](clojure.core-api.html#clojure.core/group-by)[halt-when](clojure.core-api.html#clojure.core/halt-when)[hash](clojure.core-api.html#clojure.core/hash)[hash-map](clojure.core-api.html#clojure.core/hash-map)[hash-ordered-coll](clojure.core-api.html#clojure.core/hash-ordered-coll)[hash-set](clojure.core-api.html#clojure.core/hash-set)[hash-unordered-coll](clojure.core-api.html#clojure.core/hash-unordered-coll)[ident?](clojure.core-api.html#clojure.core/ident?)[identical?](clojure.core-api.html#clojure.core/identical?)[identity](clojure.core-api.html#clojure.core/identity)[if](clojure.core-api.html#clojure.core/if)[if-let](clojure.core-api.html#clojure.core/if-let)[if-not](clojure.core-api.html#clojure.core/if-not)[if-some](clojure.core-api.html#clojure.core/if-some)[ifn?](clojure.core-api.html#clojure.core/ifn?)[import](clojure.core-api.html#clojure.core/import)[in-ns](clojure.core-api.html#clojure.core/in-ns)[inc](clojure.core-api.html#clojure.core/inc)[inc'](clojure.core-api.html#clojure.core/inc')[indexed?](clojure.core-api.html#clojure.core/indexed?)[infinite?](clojure.core-api.html#clojure.core/infinite?)[init-proxy](clojure.core-api.html#clojure.core/init-proxy)[inst-ms](clojure.core-api.html#clojure.core/inst-ms)[inst?](clojure.core-api.html#clojure.core/inst?)[instance?](clojure.core-api.html#clojure.core/instance?)[int](clojure.core-api.html#clojure.core/int)[int-array](clojure.core-api.html#clojure.core/int-array)[int?](clojure.core-api.html#clojure.core/int?)[integer?](clojure.core-api.html#clojure.core/integer?)[interleave](clojure.core-api.html#clojure.core/interleave)[intern](clojure.core-api.html#clojure.core/intern)[interpose](clojure.core-api.html#clojure.core/interpose)[into](clojure.core-api.html#clojure.core/into)[into-array](clojure.core-api.html#clojure.core/into-array)[ints](clojure.core-api.html#clojure.core/ints)[io!](clojure.core-api.html#clojure.core/io!)[isa?](clojure.core-api.html#clojure.core/isa?)[iterate](clojure.core-api.html#clojure.core/iterate)[iteration](clojure.core-api.html#clojure.core/iteration)[iterator-seq](clojure.core-api.html#clojure.core/iterator-seq)[juxt](clojure.core-api.html#clojure.core/juxt)[keep](clojure.core-api.html#clojure.core/keep)[keep-indexed](clojure.core-api.html#clojure.core/keep-indexed)[key](clojure.core-api.html#clojure.core/key)[keys](clojure.core-api.html#clojure.core/keys)[keyword](clojure.core-api.html#clojure.core/keyword)[keyword?](clojure.core-api.html#clojure.core/keyword?)[last](clojure.core-api.html#clojure.core/last)[lazy-cat](clojure.core-api.html#clojure.core/lazy-cat)[lazy-seq](clojure.core-api.html#clojure.core/lazy-seq)[let](clojure.core-api.html#clojure.core/let)[letfn](clojure.core-api.html#clojure.core/letfn)[line-seq](clojure.core-api.html#clojure.core/line-seq)[list](clojure.core-api.html#clojure.core/list)[list*](clojure.core-api.html#clojure.core/list*)[list?](clojure.core-api.html#clojure.core/list?)[load](clojure.core-api.html#clojure.core/load)[load-file](clojure.core-api.html#clojure.core/load-file)[load-reader](clojure.core-api.html#clojure.core/load-reader)[load-string](clojure.core-api.html#clojure.core/load-string)[loaded-libs](clojure.core-api.html#clojure.core/loaded-libs)[locking](clojure.core-api.html#clojure.core/locking)[long](clojure.core-api.html#clojure.core/long)[long-array](clojure.core-api.html#clojure.core/long-array)[longs](clojure.core-api.html#clojure.core/longs)[loop](clojure.core-api.html#clojure.core/loop)[macroexpand](clojure.core-api.html#clojure.core/macroexpand)[macroexpand-1](clojure.core-api.html#clojure.core/macroexpand-1)[make-array](clojure.core-api.html#clojure.core/make-array)[make-hierarchy](clojure.core-api.html#clojure.core/make-hierarchy)[map](clojure.core-api.html#clojure.core/map)[map-entry?](clojure.core-api.html#clojure.core/map-entry?)[map-indexed](clojure.core-api.html#clojure.core/map-indexed)[map?](clojure.core-api.html#clojure.core/map?)[mapcat](clojure.core-api.html#clojure.core/mapcat)[mapv](clojure.core-api.html#clojure.core/mapv)[max](clojure.core-api.html#clojure.core/max)[max-key](clojure.core-api.html#clojure.core/max-key)[memfn](clojure.core-api.html#clojure.core/memfn)[memoize](clojure.core-api.html#clojure.core/memoize)[merge](clojure.core-api.html#clojure.core/merge)[merge-with](clojure.core-api.html#clojure.core/merge-with)[meta](clojure.core-api.html#clojure.core/meta)[methods](clojure.core-api.html#clojure.core/methods)[min](clojure.core-api.html#clojure.core/min)[min-key](clojure.core-api.html#clojure.core/min-key)[mix-collection-hash](clojure.core-api.html#clojure.core/mix-collection-hash)[mod](clojure.core-api.html#clojure.core/mod)[monitor-enter](clojure.core-api.html#clojure.core/monitor-enter)[monitor-exit](clojure.core-api.html#clojure.core/monitor-exit)[name](clojure.core-api.html#clojure.core/name)[namespace](clojure.core-api.html#clojure.core/namespace)[namespace-munge](clojure.core-api.html#clojure.core/namespace-munge)[NaN?](clojure.core-api.html#clojure.core/NaN?)[nat-int?](clojure.core-api.html#clojure.core/nat-int?)[neg-int?](clojure.core-api.html#clojure.core/neg-int?)[neg?](clojure.core-api.html#clojure.core/neg?)[new](clojure.core-api.html#clojure.core/new)[newline](clojure.core-api.html#clojure.core/newline)[next](clojure.core-api.html#clojure.core/next)[nfirst](clojure.core-api.html#clojure.core/nfirst)[nil?](clojure.core-api.html#clojure.core/nil?)[nnext](clojure.core-api.html#clojure.core/nnext)[not](clojure.core-api.html#clojure.core/not)[not-any?](clojure.core-api.html#clojure.core/not-any?)[not-empty](clojure.core-api.html#clojure.core/not-empty)[not-every?](clojure.core-api.html#clojure.core/not-every?)[not=](clojure.core-api.html#clojure.core/not=)[ns](clojure.core-api.html#clojure.core/ns)[ns-aliases](clojure.core-api.html#clojure.core/ns-aliases)[ns-imports](clojure.core-api.html#clojure.core/ns-imports)[ns-interns](clojure.core-api.html#clojure.core/ns-interns)[ns-map](clojure.core-api.html#clojure.core/ns-map)[ns-name](clojure.core-api.html#clojure.core/ns-name)[ns-publics](clojure.core-api.html#clojure.core/ns-publics)[ns-refers](clojure.core-api.html#clojure.core/ns-refers)[ns-resolve](clojure.core-api.html#clojure.core/ns-resolve)[ns-unalias](clojure.core-api.html#clojure.core/ns-unalias)[ns-unmap](clojure.core-api.html#clojure.core/ns-unmap)[nth](clojure.core-api.html#clojure.core/nth)[nthnext](clojure.core-api.html#clojure.core/nthnext)[nthrest](clojure.core-api.html#clojure.core/nthrest)[num](clojure.core-api.html#clojure.core/num)[number?](clojure.core-api.html#clojure.core/number?)[numerator](clojure.core-api.html#clojure.core/numerator)[object-array](clojure.core-api.html#clojure.core/object-array)[odd?](clojure.core-api.html#clojure.core/odd?)[or](clojure.core-api.html#clojure.core/or)[parents](clojure.core-api.html#clojure.core/parents)[parse-boolean](clojure.core-api.html#clojure.core/parse-boolean)[parse-double](clojure.core-api.html#clojure.core/parse-double)[parse-long](clojure.core-api.html#clojure.core/parse-long)[parse-uuid](clojure.core-api.html#clojure.core/parse-uuid)[partial](clojure.core-api.html#clojure.core/partial)[partition](clojure.core-api.html#clojure.core/partition)[partition-all](clojure.core-api.html#clojure.core/partition-all)[partition-by](clojure.core-api.html#clojure.core/partition-by)[partitionv](clojure.core-api.html#clojure.core/partitionv)[partitionv-all](clojure.core-api.html#clojure.core/partitionv-all)[pcalls](clojure.core-api.html#clojure.core/pcalls)[peek](clojure.core-api.html#clojure.core/peek)[persistent!](clojure.core-api.html#clojure.core/persistent!)[pmap](clojure.core-api.html#clojure.core/pmap)[pop](clojure.core-api.html#clojure.core/pop)[pop!](clojure.core-api.html#clojure.core/pop!)[pop-thread-bindings](clojure.core-api.html#clojure.core/pop-thread-bindings)[pos-int?](clojure.core-api.html#clojure.core/pos-int?)[pos?](clojure.core-api.html#clojure.core/pos?)[pr](clojure.core-api.html#clojure.core/pr)[pr-str](clojure.core-api.html#clojure.core/pr-str)[prefer-method](clojure.core-api.html#clojure.core/prefer-method)[prefers](clojure.core-api.html#clojure.core/prefers)[print](clojure.core-api.html#clojure.core/print)[print-str](clojure.core-api.html#clojure.core/print-str)[printf](clojure.core-api.html#clojure.core/printf)[println](clojure.core-api.html#clojure.core/println)[println-str](clojure.core-api.html#clojure.core/println-str)[PrintWriter-on](clojure.core-api.html#clojure.core/PrintWriter-on)[prn](clojure.core-api.html#clojure.core/prn)[prn-str](clojure.core-api.html#clojure.core/prn-str)[promise](clojure.core-api.html#clojure.core/promise)[proxy](clojure.core-api.html#clojure.core/proxy)[proxy-mappings](clojure.core-api.html#clojure.core/proxy-mappings)[proxy-super](clojure.core-api.html#clojure.core/proxy-super)[push-thread-bindings](clojure.core-api.html#clojure.core/push-thread-bindings)[pvalues](clojure.core-api.html#clojure.core/pvalues)[qualified-ident?](clojure.core-api.html#clojure.core/qualified-ident?)[qualified-keyword?](clojure.core-api.html#clojure.core/qualified-keyword?)[qualified-symbol?](clojure.core-api.html#clojure.core/qualified-symbol?)[quot](clojure.core-api.html#clojure.core/quot)[quote](clojure.core-api.html#clojure.core/quote)[rand](clojure.core-api.html#clojure.core/rand)[rand-int](clojure.core-api.html#clojure.core/rand-int)[rand-nth](clojure.core-api.html#clojure.core/rand-nth)[random-sample](clojure.core-api.html#clojure.core/random-sample)[random-uuid](clojure.core-api.html#clojure.core/random-uuid)[range](clojure.core-api.html#clojure.core/range)[ratio?](clojure.core-api.html#clojure.core/ratio?)[rational?](clojure.core-api.html#clojure.core/rational?)[rationalize](clojure.core-api.html#clojure.core/rationalize)[re-find](clojure.core-api.html#clojure.core/re-find)[re-groups](clojure.core-api.html#clojure.core/re-groups)[re-matcher](clojure.core-api.html#clojure.core/re-matcher)[re-matches](clojure.core-api.html#clojure.core/re-matches)[re-pattern](clojure.core-api.html#clojure.core/re-pattern)[re-seq](clojure.core-api.html#clojure.core/re-seq)[read](clojure.core-api.html#clojure.core/read)[read+string](clojure.core-api.html#clojure.core/read+string)[read-line](clojure.core-api.html#clojure.core/read-line)[read-string](clojure.core-api.html#clojure.core/read-string)[reader-conditional](clojure.core-api.html#clojure.core/reader-conditional)[reader-conditional?](clojure.core-api.html#clojure.core/reader-conditional?)[realized?](clojure.core-api.html#clojure.core/realized?)[record?](clojure.core-api.html#clojure.core/record?)[recur](clojure.core-api.html#clojure.core/recur)[reduce](clojure.core-api.html#clojure.core/reduce)[reduce-kv](clojure.core-api.html#clojure.core/reduce-kv)[reduced](clojure.core-api.html#clojure.core/reduced)[reduced?](clojure.core-api.html#clojure.core/reduced?)[reductions](clojure.core-api.html#clojure.core/reductions)[ref](clojure.core-api.html#clojure.core/ref)[ref-history-count](clojure.core-api.html#clojure.core/ref-history-count)[ref-max-history](clojure.core-api.html#clojure.core/ref-max-history)[ref-min-history](clojure.core-api.html#clojure.core/ref-min-history)[ref-set](clojure.core-api.html#clojure.core/ref-set)[refer](clojure.core-api.html#clojure.core/refer)[refer-clojure](clojure.core-api.html#clojure.core/refer-clojure)[reify](clojure.core-api.html#clojure.core/reify)[release-pending-sends](clojure.core-api.html#clojure.core/release-pending-sends)[rem](clojure.core-api.html#clojure.core/rem)[remove](clojure.core-api.html#clojure.core/remove)[remove-all-methods](clojure.core-api.html#clojure.core/remove-all-methods)[remove-method](clojure.core-api.html#clojure.core/remove-method)[remove-ns](clojure.core-api.html#clojure.core/remove-ns)[remove-tap](clojure.core-api.html#clojure.core/remove-tap)[remove-watch](clojure.core-api.html#clojure.core/remove-watch)[repeat](clojure.core-api.html#clojure.core/repeat)[repeatedly](clojure.core-api.html#clojure.core/repeatedly)[replace](clojure.core-api.html#clojure.core/replace)[replicate](clojure.core-api.html#clojure.core/replicate)[require](clojure.core-api.html#clojure.core/require)[requiring-resolve](clojure.core-api.html#clojure.core/requiring-resolve)[reset!](clojure.core-api.html#clojure.core/reset!)[reset-meta!](clojure.core-api.html#clojure.core/reset-meta!)[reset-vals!](clojure.core-api.html#clojure.core/reset-vals!)[resolve](clojure.core-api.html#clojure.core/resolve)[rest](clojure.core-api.html#clojure.core/rest)[restart-agent](clojure.core-api.html#clojure.core/restart-agent)[resultset-seq](clojure.core-api.html#clojure.core/resultset-seq)[reverse](clojure.core-api.html#clojure.core/reverse)[reversible?](clojure.core-api.html#clojure.core/reversible?)[rseq](clojure.core-api.html#clojure.core/rseq)[rsubseq](clojure.core-api.html#clojure.core/rsubseq)[run!](clojure.core-api.html#clojure.core/run!)[satisfies?](clojure.core-api.html#clojure.core/satisfies?)[second](clojure.core-api.html#clojure.core/second)[select-keys](clojure.core-api.html#clojure.core/select-keys)[send](clojure.core-api.html#clojure.core/send)[send-off](clojure.core-api.html#clojure.core/send-off)[send-via](clojure.core-api.html#clojure.core/send-via)[seq](clojure.core-api.html#clojure.core/seq)[seq-to-map-for-destructuring](clojure.core-api.html#clojure.core/seq-to-map-for-destructuring)[seq?](clojure.core-api.html#clojure.core/seq?)[seqable?](clojure.core-api.html#clojure.core/seqable?)[seque](clojure.core-api.html#clojure.core/seque)[sequence](clojure.core-api.html#clojure.core/sequence)[sequential?](clojure.core-api.html#clojure.core/sequential?)[set](clojure.core-api.html#clojure.core/set)[set!](clojure.core-api.html#clojure.core/set!)[set-agent-send-executor!](clojure.core-api.html#clojure.core/set-agent-send-executor!)[set-agent-send-off-executor!](clojure.core-api.html#clojure.core/set-agent-send-off-executor!)[set-error-handler!](clojure.core-api.html#clojure.core/set-error-handler!)[set-error-mode!](clojure.core-api.html#clojure.core/set-error-mode!)[set-validator!](clojure.core-api.html#clojure.core/set-validator!)[set?](clojure.core-api.html#clojure.core/set?)[short](clojure.core-api.html#clojure.core/short)[short-array](clojure.core-api.html#clojure.core/short-array)[shorts](clojure.core-api.html#clojure.core/shorts)[shuffle](clojure.core-api.html#clojure.core/shuffle)[shutdown-agents](clojure.core-api.html#clojure.core/shutdown-agents)[simple-ident?](clojure.core-api.html#clojure.core/simple-ident?)[simple-keyword?](clojure.core-api.html#clojure.core/simple-keyword?)[simple-symbol?](clojure.core-api.html#clojure.core/simple-symbol?)[slurp](clojure.core-api.html#clojure.core/slurp)[some](clojure.core-api.html#clojure.core/some)[some->](clojure.core-api.html#clojure.core/some->)[some->>](clojure.core-api.html#clojure.core/some->>)[some-fn](clojure.core-api.html#clojure.core/some-fn)[some?](clojure.core-api.html#clojure.core/some?)[sort](clojure.core-api.html#clojure.core/sort)[sort-by](clojure.core-api.html#clojure.core/sort-by)[sorted-map](clojure.core-api.html#clojure.core/sorted-map)[sorted-map-by](clojure.core-api.html#clojure.core/sorted-map-by)[sorted-set](clojure.core-api.html#clojure.core/sorted-set)[sorted-set-by](clojure.core-api.html#clojure.core/sorted-set-by)[sorted?](clojure.core-api.html#clojure.core/sorted?)[special-symbol?](clojure.core-api.html#clojure.core/special-symbol?)[spit](clojure.core-api.html#clojure.core/spit)[split-at](clojure.core-api.html#clojure.core/split-at)[split-with](clojure.core-api.html#clojure.core/split-with)[splitv-at](clojure.core-api.html#clojure.core/splitv-at)[StackTraceElement->vec](clojure.core-api.html#clojure.core/StackTraceElement->vec)[str](clojure.core-api.html#clojure.core/str)[stream-into!](clojure.core-api.html#clojure.core/stream-into!)[stream-reduce!](clojure.core-api.html#clojure.core/stream-reduce!)[stream-seq!](clojure.core-api.html#clojure.core/stream-seq!)[stream-transduce!](clojure.core-api.html#clojure.core/stream-transduce!)[string?](clojure.core-api.html#clojure.core/string?)[struct](clojure.core-api.html#clojure.core/struct)[struct-map](clojure.core-api.html#clojure.core/struct-map)[subs](clojure.core-api.html#clojure.core/subs)[subseq](clojure.core-api.html#clojure.core/subseq)[subvec](clojure.core-api.html#clojure.core/subvec)[supers](clojure.core-api.html#clojure.core/supers)[swap!](clojure.core-api.html#clojure.core/swap!)[swap-vals!](clojure.core-api.html#clojure.core/swap-vals!)[symbol](clojure.core-api.html#clojure.core/symbol)[symbol?](clojure.core-api.html#clojure.core/symbol?)[sync](clojure.core-api.html#clojure.core/sync)[tagged-literal](clojure.core-api.html#clojure.core/tagged-literal)[tagged-literal?](clojure.core-api.html#clojure.core/tagged-literal?)[take](clojure.core-api.html#clojure.core/take)[take-last](clojure.core-api.html#clojure.core/take-last)[take-nth](clojure.core-api.html#clojure.core/take-nth)[take-while](clojure.core-api.html#clojure.core/take-while)[tap>](clojure.core-api.html#clojure.core/tap>)[test](clojure.core-api.html#clojure.core/test)[the-ns](clojure.core-api.html#clojure.core/the-ns)[thread-bound?](clojure.core-api.html#clojure.core/thread-bound?)[throw](clojure.core-api.html#clojure.core/throw)[Throwable->map](clojure.core-api.html#clojure.core/Throwable->map)[time](clojure.core-api.html#clojure.core/time)[to-array](clojure.core-api.html#clojure.core/to-array)[to-array-2d](clojure.core-api.html#clojure.core/to-array-2d)[trampoline](clojure.core-api.html#clojure.core/trampoline)[transduce](clojure.core-api.html#clojure.core/transduce)[transient](clojure.core-api.html#clojure.core/transient)[tree-seq](clojure.core-api.html#clojure.core/tree-seq)[true?](clojure.core-api.html#clojure.core/true?)[try](clojure.core-api.html#clojure.core/try)[type](clojure.core-api.html#clojure.core/type)[unchecked-add](clojure.core-api.html#clojure.core/unchecked-add)[unchecked-add-int](clojure.core-api.html#clojure.core/unchecked-add-int)[unchecked-byte](clojure.core-api.html#clojure.core/unchecked-byte)[unchecked-char](clojure.core-api.html#clojure.core/unchecked-char)[unchecked-dec](clojure.core-api.html#clojure.core/unchecked-dec)[unchecked-dec-int](clojure.core-api.html#clojure.core/unchecked-dec-int)[unchecked-divide-int](clojure.core-api.html#clojure.core/unchecked-divide-int)[unchecked-double](clojure.core-api.html#clojure.core/unchecked-double)[unchecked-float](clojure.core-api.html#clojure.core/unchecked-float)[unchecked-inc](clojure.core-api.html#clojure.core/unchecked-inc)[unchecked-inc-int](clojure.core-api.html#clojure.core/unchecked-inc-int)[unchecked-int](clojure.core-api.html#clojure.core/unchecked-int)[unchecked-long](clojure.core-api.html#clojure.core/unchecked-long)[unchecked-multiply](clojure.core-api.html#clojure.core/unchecked-multiply)[unchecked-multiply-int](clojure.core-api.html#clojure.core/unchecked-multiply-int)[unchecked-negate](clojure.core-api.html#clojure.core/unchecked-negate)[unchecked-negate-int](clojure.core-api.html#clojure.core/unchecked-negate-int)[unchecked-remainder-int](clojure.core-api.html#clojure.core/unchecked-remainder-int)[unchecked-short](clojure.core-api.html#clojure.core/unchecked-short)[unchecked-subtract](clojure.core-api.html#clojure.core/unchecked-subtract)[unchecked-subtract-int](clojure.core-api.html#clojure.core/unchecked-subtract-int)[underive](clojure.core-api.html#clojure.core/underive)[unreduced](clojure.core-api.html#clojure.core/unreduced)[unsigned-bit-shift-right](clojure.core-api.html#clojure.core/unsigned-bit-shift-right)[update](clojure.core-api.html#clojure.core/update)[update-in](clojure.core-api.html#clojure.core/update-in)[update-keys](clojure.core-api.html#clojure.core/update-keys)[update-proxy](clojure.core-api.html#clojure.core/update-proxy)[update-vals](clojure.core-api.html#clojure.core/update-vals)[uri?](clojure.core-api.html#clojure.core/uri?)[use](clojure.core-api.html#clojure.core/use)[uuid?](clojure.core-api.html#clojure.core/uuid?)[val](clojure.core-api.html#clojure.core/val)[vals](clojure.core-api.html#clojure.core/vals)[var](clojure.core-api.html#clojure.core/var)[var-get](clojure.core-api.html#clojure.core/var-get)[var-set](clojure.core-api.html#clojure.core/var-set)[var?](clojure.core-api.html#clojure.core/var?)[vary-meta](clojure.core-api.html#clojure.core/vary-meta)[vec](clojure.core-api.html#clojure.core/vec)[Vec](clojure.core-api.html#clojure.core/Vec)[VecNode](clojure.core-api.html#clojure.core/VecNode)[VecSeq](clojure.core-api.html#clojure.core/VecSeq)[vector](clojure.core-api.html#clojure.core/vector)[vector-of](clojure.core-api.html#clojure.core/vector-of)[vector?](clojure.core-api.html#clojure.core/vector?)[volatile!](clojure.core-api.html#clojure.core/volatile!)[volatile?](clojure.core-api.html#clojure.core/volatile?)[vreset!](clojure.core-api.html#clojure.core/vreset!)[vswap!](clojure.core-api.html#clojure.core/vswap!)[when](clojure.core-api.html#clojure.core/when)[when-first](clojure.core-api.html#clojure.core/when-first)[when-let](clojure.core-api.html#clojure.core/when-let)[when-not](clojure.core-api.html#clojure.core/when-not)[when-some](clojure.core-api.html#clojure.core/when-some)[while](clojure.core-api.html#clojure.core/while)[with-bindings](clojure.core-api.html#clojure.core/with-bindings)[with-bindings*](clojure.core-api.html#clojure.core/with-bindings*)[with-in-str](clojure.core-api.html#clojure.core/with-in-str)[with-local-vars](clojure.core-api.html#clojure.core/with-local-vars)[with-meta](clojure.core-api.html#clojure.core/with-meta)[with-open](clojure.core-api.html#clojure.core/with-open)[with-out-str](clojure.core-api.html#clojure.core/with-out-str)[with-precision](clojure.core-api.html#clojure.core/with-precision)[with-redefs](clojure.core-api.html#clojure.core/with-redefs)[with-redefs-fn](clojure.core-api.html#clojure.core/with-redefs-fn)[xml-seq](clojure.core-api.html#clojure.core/xml-seq)[zero?](clojure.core-api.html#clojure.core/zero?)[zipmap](clojure.core-api.html#clojure.core/zipmap)

Variables and functions in clojure.core.protocols: [coll-reduce](clojure.core-api.html#clojure.core.protocols/coll-reduce)[CollReduce](clojure.core-api.html#clojure.core.protocols/CollReduce)[Datafiable](clojure.core-api.html#clojure.core.protocols/Datafiable)[datafy](clojure.core-api.html#clojure.core.protocols/datafy)[IKVReduce](clojure.core-api.html#clojure.core.protocols/IKVReduce)[internal-reduce](clojure.core-api.html#clojure.core.protocols/internal-reduce)[InternalReduce](clojure.core-api.html#clojure.core.protocols/InternalReduce)[kv-reduce](clojure.core-api.html#clojure.core.protocols/kv-reduce)[nav](clojure.core-api.html#clojure.core.protocols/nav)[Navigable](clojure.core-api.html#clojure.core.protocols/Navigable)

Variables and functions in clojure.core.reducers: [->Cat](clojure.core-api.html#clojure.core.reducers/->Cat)[append!](clojure.core-api.html#clojure.core.reducers/append!)[cat](clojure.core-api.html#clojure.core.reducers/cat)[Cat](clojure.core-api.html#clojure.core.reducers/Cat)[drop](clojure.core-api.html#clojure.core.reducers/drop)[filter](clojure.core-api.html#clojure.core.reducers/filter)[flatten](clojure.core-api.html#clojure.core.reducers/flatten)[fold](clojure.core-api.html#clojure.core.reducers/fold)[foldcat](clojure.core-api.html#clojure.core.reducers/foldcat)[folder](clojure.core-api.html#clojure.core.reducers/folder)[map](clojure.core-api.html#clojure.core.reducers/map)[mapcat](clojure.core-api.html#clojure.core.reducers/mapcat)[monoid](clojure.core-api.html#clojure.core.reducers/monoid)[reduce](clojure.core-api.html#clojure.core.reducers/reduce)[reducer](clojure.core-api.html#clojure.core.reducers/reducer)[remove](clojure.core-api.html#clojure.core.reducers/remove)[take](clojure.core-api.html#clojure.core.reducers/take)[take-while](clojure.core-api.html#clojure.core.reducers/take-while)

Variables and functions in clojure.core.server: [io-prepl](clojure.core-api.html#clojure.core.server/io-prepl)[prepl](clojure.core-api.html#clojure.core.server/prepl)[remote-prepl](clojure.core-api.html#clojure.core.server/remote-prepl)[repl](clojure.core-api.html#clojure.core.server/repl)[repl-init](clojure.core-api.html#clojure.core.server/repl-init)[repl-read](clojure.core-api.html#clojure.core.server/repl-read)[start-server](clojure.core-api.html#clojure.core.server/start-server)[start-servers](clojure.core-api.html#clojure.core.server/start-servers)[stop-server](clojure.core-api.html#clojure.core.server/stop-server)[stop-servers](clojure.core-api.html#clojure.core.server/stop-servers)

Variables and functions in clojure.core.specs.alpha: [::as](clojure.core-api.html#:clojure.core.specs.alpha/as)[::as-alias](clojure.core-api.html#:clojure.core.specs.alpha/as-alias)[::binding](clojure.core-api.html#:clojure.core.specs.alpha/binding)[::binding-form](clojure.core-api.html#:clojure.core.specs.alpha/binding-form)[::bindings](clojure.core-api.html#:clojure.core.specs.alpha/bindings)[::class-ident](clojure.core-api.html#:clojure.core.specs.alpha/class-ident)[::constructors](clojure.core-api.html#:clojure.core.specs.alpha/constructors)[::defn-args](clojure.core-api.html#:clojure.core.specs.alpha/defn-args)[even-number-of-forms?](clojure.core-api.html#clojure.core.specs.alpha/even-number-of-forms?)[::exclude](clojure.core-api.html#:clojure.core.specs.alpha/exclude)[::expose](clojure.core-api.html#:clojure.core.specs.alpha/expose)[::exposes](clojure.core-api.html#:clojure.core.specs.alpha/exposes)[::extends](clojure.core-api.html#:clojure.core.specs.alpha/extends)[::factory](clojure.core-api.html#:clojure.core.specs.alpha/factory)[::filters](clojure.core-api.html#:clojure.core.specs.alpha/filters)[::get](clojure.core-api.html#:clojure.core.specs.alpha/get)[::impl-ns](clojure.core-api.html#:clojure.core.specs.alpha/impl-ns)[::implements](clojure.core-api.html#:clojure.core.specs.alpha/implements)[::import-list](clojure.core-api.html#:clojure.core.specs.alpha/import-list)[::init](clojure.core-api.html#:clojure.core.specs.alpha/init)[::keys](clojure.core-api.html#:clojure.core.specs.alpha/keys)[::libspec](clojure.core-api.html#:clojure.core.specs.alpha/libspec)[::load-impl-ns](clojure.core-api.html#:clojure.core.specs.alpha/load-impl-ns)[::local-name](clojure.core-api.html#:clojure.core.specs.alpha/local-name)[::main](clojure.core-api.html#:clojure.core.specs.alpha/main)[::map-binding](clojure.core-api.html#:clojure.core.specs.alpha/map-binding)[::map-binding-form](clojure.core-api.html#:clojure.core.specs.alpha/map-binding-form)[::map-bindings](clojure.core-api.html#:clojure.core.specs.alpha/map-bindings)[::map-special-binding](clojure.core-api.html#:clojure.core.specs.alpha/map-special-binding)[::method](clojure.core-api.html#:clojure.core.specs.alpha/method)[::methods](clojure.core-api.html#:clojure.core.specs.alpha/methods)[::name](clojure.core-api.html#:clojure.core.specs.alpha/name)[::ns-clauses](clojure.core-api.html#:clojure.core.specs.alpha/ns-clauses)[::ns-form](clojure.core-api.html#:clojure.core.specs.alpha/ns-form)[::ns-gen-class](clojure.core-api.html#:clojure.core.specs.alpha/ns-gen-class)[::ns-import](clojure.core-api.html#:clojure.core.specs.alpha/ns-import)[::ns-keys](clojure.core-api.html#:clojure.core.specs.alpha/ns-keys)[::ns-load](clojure.core-api.html#:clojure.core.specs.alpha/ns-load)[::ns-refer](clojure.core-api.html#:clojure.core.specs.alpha/ns-refer)[::ns-refer-clojure](clojure.core-api.html#:clojure.core.specs.alpha/ns-refer-clojure)[::ns-require](clojure.core-api.html#:clojure.core.specs.alpha/ns-require)[::ns-use](clojure.core-api.html#:clojure.core.specs.alpha/ns-use)[::only](clojure.core-api.html#:clojure.core.specs.alpha/only)[::or](clojure.core-api.html#:clojure.core.specs.alpha/or)[::package-list](clojure.core-api.html#:clojure.core.specs.alpha/package-list)[::param-list](clojure.core-api.html#:clojure.core.specs.alpha/param-list)[::params+body](clojure.core-api.html#:clojure.core.specs.alpha/params+body)[::post-init](clojure.core-api.html#:clojure.core.specs.alpha/post-init)[::prefix](clojure.core-api.html#:clojure.core.specs.alpha/prefix)[::prefix-list](clojure.core-api.html#:clojure.core.specs.alpha/prefix-list)[::quotable-import-list](clojure.core-api.html#:clojure.core.specs.alpha/quotable-import-list)[::refer](clojure.core-api.html#:clojure.core.specs.alpha/refer)[::rename](clojure.core-api.html#:clojure.core.specs.alpha/rename)[::seq-binding-form](clojure.core-api.html#:clojure.core.specs.alpha/seq-binding-form)[::set](clojure.core-api.html#:clojure.core.specs.alpha/set)[::signature](clojure.core-api.html#:clojure.core.specs.alpha/signature)[::state](clojure.core-api.html#:clojure.core.specs.alpha/state)[::strs](clojure.core-api.html#:clojure.core.specs.alpha/strs)[::syms](clojure.core-api.html#:clojure.core.specs.alpha/syms)[::use-libspec](clojure.core-api.html#:clojure.core.specs.alpha/use-libspec)[::use-prefix-list](clojure.core-api.html#:clojure.core.specs.alpha/use-prefix-list)

## clojure.data

by Stuart Halloway
[Detailed API documentation](clojure.data-api.html)

```
Non-core data functions.
```

 Contents: [diff](clojure.data-api.html#clojure.data/diff)[Diff](clojure.data-api.html#clojure.data/Diff)[diff-similar](clojure.data-api.html#clojure.data/diff-similar)[equality-partition](clojure.data-api.html#clojure.data/equality-partition)[EqualityPartition](clojure.data-api.html#clojure.data/EqualityPartition)

## clojure.datafy

[Detailed API documentation](clojure.datafy-api.html)

```
Functions to turn objects into data. Alpha, subject to change
```

 Contents: [datafy](clojure.datafy-api.html#clojure.datafy/datafy)[nav](clojure.datafy-api.html#clojure.datafy/nav)

## clojure.edn

by Rich Hickey
[Detailed API documentation](clojure.edn-api.html)

```
edn reading.
```

 Contents: [read](clojure.edn-api.html#clojure.edn/read)[read-string](clojure.edn-api.html#clojure.edn/read-string)

## clojure.inspector

by Rich Hickey
[Detailed API documentation](clojure.inspector-api.html)

```
Graphical object inspector for Clojure data structures.
```

 Contents: [inspect](clojure.inspector-api.html#clojure.inspector/inspect)[inspect-table](clojure.inspector-api.html#clojure.inspector/inspect-table)[inspect-tree](clojure.inspector-api.html#clojure.inspector/inspect-tree)

## clojure.instant

[Detailed API documentation](clojure.instant-api.html)

```
```

 Contents: [parse-timestamp](clojure.instant-api.html#clojure.instant/parse-timestamp)[read-instant-calendar](clojure.instant-api.html#clojure.instant/read-instant-calendar)[read-instant-date](clojure.instant-api.html#clojure.instant/read-instant-date)[read-instant-timestamp](clojure.instant-api.html#clojure.instant/read-instant-timestamp)[validated](clojure.instant-api.html#clojure.instant/validated)

## clojure.java.basis

[Detailed API documentation](clojure.java.basis-api.html)

```
The lib basis includes which libraries and versions were loaded both
for direct dependencies and transitive dependencies, as well as the
classpath and possibly other information from the resolution process.
This basis will be known if the runtime was started by the Clojure CLI.

The Clojure CLI or tools.deps merge a set of deps maps (often from
deps.edn files). Additional runtime modifications are supplied via argmap
keys, provided via alias maps in the merged deps. Deps maps typically have
:paths, :deps, and :aliases keys.

The basis is a superset of merged deps.edn files with the following
additional keys:
  :basis-config - params used to configure basis deps sources, can be
                  string path, deps map, nil, or :default
    :root - default = loaded as a resource from tools.deps)
    :user - default = ~/.clojure/deps.edn)
    :project - default = ./deps.edn)
    :extra - default = nil
    :aliases - coll of keyword aliases to include during dep calculation
  :argmap - effective argmap (after resolving and merging argmaps from aliases)
  :libs - map of lib to coord for all included libraries
  :classpath - classpath map, keys are paths (to directory or .jar), values
               are maps with source identifier (either :lib-name or :path-key)
  :classpath-roots - vector of paths in classpath order (keys of :classpath)
```

 Contents: [current-basis](clojure.java.basis-api.html#clojure.java.basis/current-basis)[initial-basis](clojure.java.basis-api.html#clojure.java.basis/initial-basis)

Variables and functions in clojure.java.basis.impl: [update-basis!](clojure.java.basis-api.html#clojure.java.basis.impl/update-basis!)

## clojure.java.browse

by Christophe Grand
[Detailed API documentation](clojure.java.browse-api.html)

```
Start a web browser from Clojure
```

 Contents: [browse-url](clojure.java.browse-api.html#clojure.java.browse/browse-url)

## clojure.java.io

by Stuart Sierra, Chas Emerick, Stuart Halloway
[Detailed API documentation](clojure.java.io-api.html)

```
This file defines polymorphic I/O utility functions for Clojure.
```

 Contents: [as-file](clojure.java.io-api.html#clojure.java.io/as-file)[as-relative-path](clojure.java.io-api.html#clojure.java.io/as-relative-path)[as-url](clojure.java.io-api.html#clojure.java.io/as-url)[Coercions](clojure.java.io-api.html#clojure.java.io/Coercions)[copy](clojure.java.io-api.html#clojure.java.io/copy)[delete-file](clojure.java.io-api.html#clojure.java.io/delete-file)[file](clojure.java.io-api.html#clojure.java.io/file)[input-stream](clojure.java.io-api.html#clojure.java.io/input-stream)[IOFactory](clojure.java.io-api.html#clojure.java.io/IOFactory)[make-input-stream](clojure.java.io-api.html#clojure.java.io/make-input-stream)[make-output-stream](clojure.java.io-api.html#clojure.java.io/make-output-stream)[make-parents](clojure.java.io-api.html#clojure.java.io/make-parents)[make-reader](clojure.java.io-api.html#clojure.java.io/make-reader)[make-writer](clojure.java.io-api.html#clojure.java.io/make-writer)[output-stream](clojure.java.io-api.html#clojure.java.io/output-stream)[reader](clojure.java.io-api.html#clojure.java.io/reader)[resource](clojure.java.io-api.html#clojure.java.io/resource)[writer](clojure.java.io-api.html#clojure.java.io/writer)

## clojure.java.javadoc

by Christophe Grand, Stuart Sierra
[Detailed API documentation](clojure.java.javadoc-api.html)

```
A repl helper to quickly open javadocs.
```

 Contents: [add-local-javadoc](clojure.java.javadoc-api.html#clojure.java.javadoc/add-local-javadoc)[add-remote-javadoc](clojure.java.javadoc-api.html#clojure.java.javadoc/add-remote-javadoc)[javadoc](clojure.java.javadoc-api.html#clojure.java.javadoc/javadoc)

## clojure.java.process

[Detailed API documentation](clojure.java.process-api.html)

```
A process invocation API wrapping the Java process API.

The primary function is 'start' which starts a process and handles the
streams as directed. It returns the Process object. Use 'exit-ref' to wait
for completion and receive the exit value, and ‘stdout', 'stderr', 'stdin'
to access the process streams. The 'exec' function handles the common case
to 'start' a process, wait for process exit, and return stdout.
```

 Contents: [exec](clojure.java.process-api.html#clojure.java.process/exec)[exit-ref](clojure.java.process-api.html#clojure.java.process/exit-ref)[from-file](clojure.java.process-api.html#clojure.java.process/from-file)[start](clojure.java.process-api.html#clojure.java.process/start)[stderr](clojure.java.process-api.html#clojure.java.process/stderr)[stdin](clojure.java.process-api.html#clojure.java.process/stdin)[stdout](clojure.java.process-api.html#clojure.java.process/stdout)[to-file](clojure.java.process-api.html#clojure.java.process/to-file)

## clojure.java.shell

by Chris Houser, Stuart Halloway
[Detailed API documentation](clojure.java.shell-api.html)

```
Conveniently launch a sub-process providing its stdin and
collecting its stdout
```

 Contents: [sh](clojure.java.shell-api.html#clojure.java.shell/sh)[with-sh-dir](clojure.java.shell-api.html#clojure.java.shell/with-sh-dir)[with-sh-env](clojure.java.shell-api.html#clojure.java.shell/with-sh-env)

## clojure.main

by Stephen C. Gilardi and Rich Hickey
[Detailed API documentation](clojure.main-api.html)

```
Top-level main function for Clojure REPL and scripts.
```

 Contents: [demunge](clojure.main-api.html#clojure.main/demunge)[err->msg](clojure.main-api.html#clojure.main/err->msg)[ex-str](clojure.main-api.html#clojure.main/ex-str)[ex-triage](clojure.main-api.html#clojure.main/ex-triage)[load-script](clojure.main-api.html#clojure.main/load-script)[main](clojure.main-api.html#clojure.main/main)[renumbering-read](clojure.main-api.html#clojure.main/renumbering-read)[repl](clojure.main-api.html#clojure.main/repl)[repl-caught](clojure.main-api.html#clojure.main/repl-caught)[repl-exception](clojure.main-api.html#clojure.main/repl-exception)[repl-prompt](clojure.main-api.html#clojure.main/repl-prompt)[repl-read](clojure.main-api.html#clojure.main/repl-read)[repl-requires](clojure.main-api.html#clojure.main/repl-requires)[report-error](clojure.main-api.html#clojure.main/report-error)[root-cause](clojure.main-api.html#clojure.main/root-cause)[skip-if-eol](clojure.main-api.html#clojure.main/skip-if-eol)[skip-whitespace](clojure.main-api.html#clojure.main/skip-whitespace)[stack-element-str](clojure.main-api.html#clojure.main/stack-element-str)[with-bindings](clojure.main-api.html#clojure.main/with-bindings)[with-read-known](clojure.main-api.html#clojure.main/with-read-known)

## clojure.math

by Alex Miller
[Detailed API documentation](clojure.math-api.html)

```
Clojure wrapper functions for java.lang.Math static methods.

Function calls are inlined for performance, and type hinted for primitive
long or double parameters where appropriate. In general, Math methods are
optimized for performance and have bounds for error tolerance. If
greater precision is needed, use java.lang.StrictMath directly instead.

For more complete information, see:
https://docs.oracle.com/javase/8/docs/api/java/lang/Math.htmlhttps://docs.oracle.com/javase/8/docs/api/java/lang/Math.html
```

 Contents: [acos](clojure.math-api.html#clojure.math/acos)[add-exact](clojure.math-api.html#clojure.math/add-exact)[asin](clojure.math-api.html#clojure.math/asin)[atan](clojure.math-api.html#clojure.math/atan)[atan2](clojure.math-api.html#clojure.math/atan2)[cbrt](clojure.math-api.html#clojure.math/cbrt)[ceil](clojure.math-api.html#clojure.math/ceil)[copy-sign](clojure.math-api.html#clojure.math/copy-sign)[cos](clojure.math-api.html#clojure.math/cos)[cosh](clojure.math-api.html#clojure.math/cosh)[decrement-exact](clojure.math-api.html#clojure.math/decrement-exact)[E](clojure.math-api.html#clojure.math/E)[exp](clojure.math-api.html#clojure.math/exp)[expm1](clojure.math-api.html#clojure.math/expm1)[floor](clojure.math-api.html#clojure.math/floor)[floor-div](clojure.math-api.html#clojure.math/floor-div)[floor-mod](clojure.math-api.html#clojure.math/floor-mod)[get-exponent](clojure.math-api.html#clojure.math/get-exponent)[hypot](clojure.math-api.html#clojure.math/hypot)[IEEE-remainder](clojure.math-api.html#clojure.math/IEEE-remainder)[increment-exact](clojure.math-api.html#clojure.math/increment-exact)[log](clojure.math-api.html#clojure.math/log)[log10](clojure.math-api.html#clojure.math/log10)[log1p](clojure.math-api.html#clojure.math/log1p)[multiply-exact](clojure.math-api.html#clojure.math/multiply-exact)[negate-exact](clojure.math-api.html#clojure.math/negate-exact)[next-after](clojure.math-api.html#clojure.math/next-after)[next-down](clojure.math-api.html#clojure.math/next-down)[next-up](clojure.math-api.html#clojure.math/next-up)[PI](clojure.math-api.html#clojure.math/PI)[pow](clojure.math-api.html#clojure.math/pow)[random](clojure.math-api.html#clojure.math/random)[rint](clojure.math-api.html#clojure.math/rint)[round](clojure.math-api.html#clojure.math/round)[scalb](clojure.math-api.html#clojure.math/scalb)[signum](clojure.math-api.html#clojure.math/signum)[sin](clojure.math-api.html#clojure.math/sin)[sinh](clojure.math-api.html#clojure.math/sinh)[sqrt](clojure.math-api.html#clojure.math/sqrt)[subtract-exact](clojure.math-api.html#clojure.math/subtract-exact)[tan](clojure.math-api.html#clojure.math/tan)[tanh](clojure.math-api.html#clojure.math/tanh)[to-degrees](clojure.math-api.html#clojure.math/to-degrees)[to-radians](clojure.math-api.html#clojure.math/to-radians)[ulp](clojure.math-api.html#clojure.math/ulp)

## clojure.pprint

by Tom Faulhaber
[Detailed API documentation](clojure.pprint-api.html)

```
A Pretty Printer for Clojure

clojure.pprint implements a flexible system for printing structured data
in a pleasing, easy-to-understand format. Basic use of the pretty printer is 
simple, just call pprint instead of println. More advanced users can use 
the building blocks provided to create custom output formats. 

Out of the box, pprint supports a simple structured format for basic data 
and a specialized format for Clojure source code. More advanced formats, 
including formats that don't look like Clojure data at all like XML and 
JSON, can be rendered by creating custom dispatch functions. 

In addition to the pprint function, this module contains cl-format, a text 
formatting function which is fully compatible with the format function in 
Common Lisp. Because pretty printing directives are directly integrated with
cl-format, it supports very concise custom dispatch. It also provides
a more powerful alternative to Clojure's standard format function.

See documentation for pprint and cl-format for more information or 
complete documentation on the Clojure web site on GitHub.
```

Added in Clojure version 1.2
 Contents: [*print-base*](clojure.pprint-api.html#clojure.pprint/*print-base*)[*print-miser-width*](clojure.pprint-api.html#clojure.pprint/*print-miser-width*)[*print-pprint-dispatch*](clojure.pprint-api.html#clojure.pprint/*print-pprint-dispatch*)[*print-pretty*](clojure.pprint-api.html#clojure.pprint/*print-pretty*)[*print-radix*](clojure.pprint-api.html#clojure.pprint/*print-radix*)[*print-right-margin*](clojure.pprint-api.html#clojure.pprint/*print-right-margin*)[*print-suppress-namespaces*](clojure.pprint-api.html#clojure.pprint/*print-suppress-namespaces*)[cl-format](clojure.pprint-api.html#clojure.pprint/cl-format)[code-dispatch](clojure.pprint-api.html#clojure.pprint/code-dispatch)[formatter](clojure.pprint-api.html#clojure.pprint/formatter)[formatter-out](clojure.pprint-api.html#clojure.pprint/formatter-out)[fresh-line](clojure.pprint-api.html#clojure.pprint/fresh-line)[get-pretty-writer](clojure.pprint-api.html#clojure.pprint/get-pretty-writer)[pp](clojure.pprint-api.html#clojure.pprint/pp)[pprint](clojure.pprint-api.html#clojure.pprint/pprint)[pprint-indent](clojure.pprint-api.html#clojure.pprint/pprint-indent)[pprint-logical-block](clojure.pprint-api.html#clojure.pprint/pprint-logical-block)[pprint-newline](clojure.pprint-api.html#clojure.pprint/pprint-newline)[pprint-tab](clojure.pprint-api.html#clojure.pprint/pprint-tab)[print-length-loop](clojure.pprint-api.html#clojure.pprint/print-length-loop)[print-table](clojure.pprint-api.html#clojure.pprint/print-table)[set-pprint-dispatch](clojure.pprint-api.html#clojure.pprint/set-pprint-dispatch)[simple-dispatch](clojure.pprint-api.html#clojure.pprint/simple-dispatch)[with-pprint-dispatch](clojure.pprint-api.html#clojure.pprint/with-pprint-dispatch)[write](clojure.pprint-api.html#clojure.pprint/write)[write-out](clojure.pprint-api.html#clojure.pprint/write-out)

## clojure.reflect

by Stuart Halloway
[Detailed API documentation](clojure.reflect-api.html)

```
Reflection on Host Types
Alpha - subject to change.

Two main entry points: 

* type-reflect reflects on something that implements TypeReference.
* reflect (for REPL use) reflects on the class of an instance, or
  on a class if passed a class

Key features:

* Exposes the read side of reflection as pure data. Reflecting
  on a type returns a map with keys :bases, :flags, and :members.

* Canonicalizes class names as Clojure symbols. Types can extend
  to the TypeReference protocol to indicate that they can be
  unambiguously resolved as a type name. The canonical format
  requires one non-Java-ish convention: array brackets are <>
  instead of [] so they can be part of a Clojure symbol.

* Pluggable Reflectors for different implementations. The default
  JavaReflector is good when you have a class in hand, or use
  the AsmReflector for "hands off" reflection without forcing
  classes to load.

Platform implementers must:

* Create an implementation of Reflector.
* Create one or more implementations of TypeReference.
* def default-reflector to be an instance that satisfies Reflector.
```

Added in Clojure version 1.3
 Contents: [->AsmReflector](clojure.reflect-api.html#clojure.reflect/->AsmReflector)[->Constructor](clojure.reflect-api.html#clojure.reflect/->Constructor)[->Field](clojure.reflect-api.html#clojure.reflect/->Field)[->JavaReflector](clojure.reflect-api.html#clojure.reflect/->JavaReflector)[->Method](clojure.reflect-api.html#clojure.reflect/->Method)[AsmReflector](clojure.reflect-api.html#clojure.reflect/AsmReflector)[ClassResolver](clojure.reflect-api.html#clojure.reflect/ClassResolver)[Constructor](clojure.reflect-api.html#clojure.reflect/Constructor)[do-reflect](clojure.reflect-api.html#clojure.reflect/do-reflect)[Field](clojure.reflect-api.html#clojure.reflect/Field)[flag-descriptors](clojure.reflect-api.html#clojure.reflect/flag-descriptors)[JavaReflector](clojure.reflect-api.html#clojure.reflect/JavaReflector)[map->Constructor](clojure.reflect-api.html#clojure.reflect/map->Constructor)[map->Field](clojure.reflect-api.html#clojure.reflect/map->Field)[map->Method](clojure.reflect-api.html#clojure.reflect/map->Method)[Method](clojure.reflect-api.html#clojure.reflect/Method)[reflect](clojure.reflect-api.html#clojure.reflect/reflect)[Reflector](clojure.reflect-api.html#clojure.reflect/Reflector)[resolve-class](clojure.reflect-api.html#clojure.reflect/resolve-class)[type-reflect](clojure.reflect-api.html#clojure.reflect/type-reflect)[typename](clojure.reflect-api.html#clojure.reflect/typename)[TypeReference](clojure.reflect-api.html#clojure.reflect/TypeReference)

## clojure.repl

by Chris Houser, Christophe Grand, Stephen Gilardi, Michel Salim
[Detailed API documentation](clojure.repl-api.html)

```
Utilities meant to be used interactively at the REPL
```

 Contents: [apropos](clojure.repl-api.html#clojure.repl/apropos)[demunge](clojure.repl-api.html#clojure.repl/demunge)[dir](clojure.repl-api.html#clojure.repl/dir)[dir-fn](clojure.repl-api.html#clojure.repl/dir-fn)[doc](clojure.repl-api.html#clojure.repl/doc)[find-doc](clojure.repl-api.html#clojure.repl/find-doc)[pst](clojure.repl-api.html#clojure.repl/pst)[root-cause](clojure.repl-api.html#clojure.repl/root-cause)[set-break-handler!](clojure.repl-api.html#clojure.repl/set-break-handler!)[source](clojure.repl-api.html#clojure.repl/source)[source-fn](clojure.repl-api.html#clojure.repl/source-fn)[stack-element-str](clojure.repl-api.html#clojure.repl/stack-element-str)[thread-stopper](clojure.repl-api.html#clojure.repl/thread-stopper)

Variables and functions in clojure.repl.deps: [add-lib](clojure.repl-api.html#clojure.repl.deps/add-lib)[add-libs](clojure.repl-api.html#clojure.repl.deps/add-libs)[sync-deps](clojure.repl-api.html#clojure.repl.deps/sync-deps)

## clojure.set

by Rich Hickey
[Detailed API documentation](clojure.set-api.html)

```
Set operations such as union/intersection.
```

 Contents: [difference](clojure.set-api.html#clojure.set/difference)[index](clojure.set-api.html#clojure.set/index)[intersection](clojure.set-api.html#clojure.set/intersection)[join](clojure.set-api.html#clojure.set/join)[map-invert](clojure.set-api.html#clojure.set/map-invert)[project](clojure.set-api.html#clojure.set/project)[rename](clojure.set-api.html#clojure.set/rename)[rename-keys](clojure.set-api.html#clojure.set/rename-keys)[select](clojure.set-api.html#clojure.set/select)[subset?](clojure.set-api.html#clojure.set/subset?)[superset?](clojure.set-api.html#clojure.set/superset?)[union](clojure.set-api.html#clojure.set/union)

## clojure.stacktrace

by Stuart Sierra
[Detailed API documentation](clojure.stacktrace-api.html)

```
Print stack traces oriented towards Clojure, not Java.
```

 Contents: [e](clojure.stacktrace-api.html#clojure.stacktrace/e)[print-cause-trace](clojure.stacktrace-api.html#clojure.stacktrace/print-cause-trace)[print-stack-trace](clojure.stacktrace-api.html#clojure.stacktrace/print-stack-trace)[print-throwable](clojure.stacktrace-api.html#clojure.stacktrace/print-throwable)[print-trace-element](clojure.stacktrace-api.html#clojure.stacktrace/print-trace-element)[root-cause](clojure.stacktrace-api.html#clojure.stacktrace/root-cause)

## clojure.string

by Stuart Sierra, Stuart Halloway, David Liebke
[Detailed API documentation](clojure.string-api.html)

```
Clojure String utilities

It is poor form to (:use clojure.string). Instead, use require
with :as to specify a prefix, e.g.

(ns your.namespace.here
  (:require [clojure.string :as str]))

Design notes for clojure.string:

1. Strings are objects (as opposed to sequences). As such, the
   string being manipulated is the first argument to a function;
   passing nil will result in a NullPointerException unless
   documented otherwise. If you want sequence-y behavior instead,
   use a sequence.

2. Functions are generally not lazy, and call straight to host
   methods where those are available and efficient.

3. Functions take advantage of String implementation details to
   write high-performing loop/recurs instead of using higher-order
   functions. (This is not idiomatic in general-purpose application
   code.)

4. When a function is documented to accept a string argument, it
   will take any implementation of the correct *interface* on the
   host platform. In Java, this is CharSequence, which is more
   general than String. In ordinary usage you will almost always
   pass concrete strings. If you are doing something unusual,
   e.g. passing a mutable implementation of CharSequence, then
   thread-safety is your responsibility.
```

 Contents: [blank?](clojure.string-api.html#clojure.string/blank?)[capitalize](clojure.string-api.html#clojure.string/capitalize)[ends-with?](clojure.string-api.html#clojure.string/ends-with?)[escape](clojure.string-api.html#clojure.string/escape)[includes?](clojure.string-api.html#clojure.string/includes?)[index-of](clojure.string-api.html#clojure.string/index-of)[join](clojure.string-api.html#clojure.string/join)[last-index-of](clojure.string-api.html#clojure.string/last-index-of)[lower-case](clojure.string-api.html#clojure.string/lower-case)[re-quote-replacement](clojure.string-api.html#clojure.string/re-quote-replacement)[replace](clojure.string-api.html#clojure.string/replace)[replace-first](clojure.string-api.html#clojure.string/replace-first)[reverse](clojure.string-api.html#clojure.string/reverse)[split](clojure.string-api.html#clojure.string/split)[split-lines](clojure.string-api.html#clojure.string/split-lines)[starts-with?](clojure.string-api.html#clojure.string/starts-with?)[trim](clojure.string-api.html#clojure.string/trim)[trim-newline](clojure.string-api.html#clojure.string/trim-newline)[triml](clojure.string-api.html#clojure.string/triml)[trimr](clojure.string-api.html#clojure.string/trimr)[upper-case](clojure.string-api.html#clojure.string/upper-case)

## clojure.template

by Stuart Sierra
[Detailed API documentation](clojure.template-api.html)

```
Macros that expand to repeated copies of a template expression.
```

 Contents: [apply-template](clojure.template-api.html#clojure.template/apply-template)[do-template](clojure.template-api.html#clojure.template/do-template)

## clojure.test

by Stuart Sierra, with contributions and suggestions by Chas Emerick, Allen Rohner, and Stuart Halloway
[Detailed API documentation](clojure.test-api.html)

```
A unit testing framework.

ASSERTIONS

The core of the library is the "is" macro, which lets you make
assertions of any arbitrary expression:

(is (= 4 (+ 2 2)))
(is (instance? Integer 256))
(is (.startsWith "abcde" "ab"))

You can type an "is" expression directly at the REPL, which will
print a message if it fails.

    user> (is (= 5 (+ 2 2)))

    FAIL in  (:1)
    expected: (= 5 (+ 2 2))
      actual: (not (= 5 4))
    false

The "expected:" line shows you the original expression, and the
"actual:" shows you what actually happened.  In this case, it
shows that (+ 2 2) returned 4, which is not = to 5.  Finally, the
"false" on the last line is the value returned from the
expression.  The "is" macro always returns the result of the
inner expression.

There are two special assertions for testing exceptions.  The
"(is (thrown? c ...))" form tests if an exception of class c is
thrown:

(is (thrown? ArithmeticException (/ 1 0))) 

"(is (thrown-with-msg? c re ...))" does the same thing and also
tests that the message on the exception matches the regular
expression re:

(is (thrown-with-msg? ArithmeticException #"Divide by zero"
                      (/ 1 0)))

DOCUMENTING TESTS

"is" takes an optional second argument, a string describing the
assertion.  This message will be included in the error report.

(is (= 5 (+ 2 2)) "Crazy arithmetic")

In addition, you can document groups of assertions with the
"testing" macro, which takes a string followed by any number of
assertions.  The string will be included in failure reports.
Calls to "testing" may be nested, and all of the strings will be
joined together with spaces in the final report, in a style
similar to RSpec <http://rspec.info/http://rspec.info/>

(testing "Arithmetic"
  (testing "with positive integers"
    (is (= 4 (+ 2 2)))
    (is (= 7 (+ 3 4))))
  (testing "with negative integers"
    (is (= -4 (+ -2 -2)))
    (is (= -1 (+ 3 -4)))))

Note that, unlike RSpec, the "testing" macro may only be used
INSIDE a "deftest" or "with-test" form (see below).

DEFINING TESTS

There are two ways to define tests.  The "with-test" macro takes
a defn or def form as its first argument, followed by any number
of assertions.  The tests will be stored as metadata on the
definition.

(with-test
    (defn my-function [x y]
      (+ x y))
  (is (= 4 (my-function 2 2)))
  (is (= 7 (my-function 3 4))))

As of Clojure SVN rev. 1221, this does not work with defmacro.
See http://code.google.com/p/clojure/issues/detail?id=51http://code.google.com/p/clojure/issues/detail?id=51

The other way lets you define tests separately from the rest of
your code, even in a different namespace:

(deftest addition
  (is (= 4 (+ 2 2)))
  (is (= 7 (+ 3 4))))

(deftest subtraction
  (is (= 1 (- 4 3)))
  (is (= 3 (- 7 4))))

This creates functions named "addition" and "subtraction", which
can be called like any other function.  Therefore, tests can be
grouped and composed, in a style similar to the test framework in
Peter Seibel's "Practical Common Lisp"
<http://www.gigamonkeys.com/book/practical-building-a-unit-test-framework.htmlhttp://www.gigamonkeys.com/book/practical-building-a-unit-test-framework.html>

(deftest arithmetic
  (addition)
  (subtraction))

The names of the nested tests will be joined in a list, like
"(arithmetic addition)", in failure reports.  You can use nested
tests to set up a context shared by several tests.

RUNNING TESTS

Run tests with the function "(run-tests namespaces...)":

(run-tests 'your.namespace 'some.other.namespace)

If you don't specify any namespaces, the current namespace is
used.  To run all tests in all namespaces, use "(run-all-tests)".

By default, these functions will search for all tests defined in
a namespace and run them in an undefined order.  However, if you
are composing tests, as in the "arithmetic" example above, you
probably do not want the "addition" and "subtraction" tests run
separately.  In that case, you must define a special function
named "test-ns-hook" that runs your tests in the correct order:

(defn test-ns-hook []
  (arithmetic))

Note: test-ns-hook prevents execution of fixtures (see below).

OMITTING TESTS FROM PRODUCTION CODE

You can bind the variable "*load-tests*" to false when loading or
compiling code in production.  This will prevent any tests from
being created by "with-test" or "deftest".

FIXTURES

Fixtures allow you to run code before and after tests, to set up
the context in which tests should be run.

A fixture is just a function that calls another function passed as
an argument.  It looks like this:

(defn my-fixture [f]
   Perform setup, establish bindings, whatever.
  (f)  Then call the function we were passed.
   Tear-down / clean-up code here.
 )

Fixtures are attached to namespaces in one of two ways.  "each"
fixtures are run repeatedly, once for each test function created
with "deftest" or "with-test".  "each" fixtures are useful for
establishing a consistent before/after state for each test, like
clearing out database tables.

"each" fixtures can be attached to the current namespace like this:
(use-fixtures :each fixture1 fixture2 ...)
The fixture1, fixture2 are just functions like the example above.
They can also be anonymous functions, like this:
(use-fixtures :each (fn [f] setup... (f) cleanup...))

The other kind of fixture, a "once" fixture, is only run once,
around ALL the tests in the namespace.  "once" fixtures are useful
for tasks that only need to be performed once, like establishing
database connections, or for time-consuming tasks.

Attach "once" fixtures to the current namespace like this:
(use-fixtures :once fixture1 fixture2 ...)

Note: Fixtures and test-ns-hook are mutually incompatible.  If you
are using test-ns-hook, fixture functions will *never* be run.

SAVING TEST OUTPUT TO A FILE

All the test reporting functions write to the var *test-out*.  By
default, this is the same as *out*, but you can rebind it to any
PrintWriter.  For example, it could be a file opened with
clojure.java.io/writer.

EXTENDING TEST-IS (ADVANCED)

You can extend the behavior of the "is" macro by defining new
methods for the "assert-expr" multimethod.  These methods are
called during expansion of the "is" macro, so they should return
quoted forms to be evaluated.

You can plug in your own test-reporting framework by rebinding
the "report" function: (report event)

The 'event' argument is a map.  It will always have a :type key,
whose value will be a keyword signaling the type of event being
reported.  Standard events with :type value of :pass, :fail, and
:error are called when an assertion passes, fails, and throws an
exception, respectively.  In that case, the event will also have
the following keys:

  :expected   The form that was expected to be true
  :actual     A form representing what actually occurred
  :message    The string message given as an argument to 'is'

The "testing" strings will be a list in "*testing-contexts*", and
the vars being tested will be a list in "*testing-vars*".

Your "report" function should wrap any printing calls in the
"with-test-out" macro, which rebinds *out* to the current value
of *test-out*.

For additional event types, see the examples in the code.
```

 Contents: [*load-tests*](clojure.test-api.html#clojure.test/*load-tests*)[*stack-trace-depth*](clojure.test-api.html#clojure.test/*stack-trace-depth*)[are](clojure.test-api.html#clojure.test/are)[assert-any](clojure.test-api.html#clojure.test/assert-any)[assert-predicate](clojure.test-api.html#clojure.test/assert-predicate)[compose-fixtures](clojure.test-api.html#clojure.test/compose-fixtures)[deftest](clojure.test-api.html#clojure.test/deftest)[deftest-](clojure.test-api.html#clojure.test/deftest-)[do-report](clojure.test-api.html#clojure.test/do-report)[file-position](clojure.test-api.html#clojure.test/file-position)[function?](clojure.test-api.html#clojure.test/function?)[get-possibly-unbound-var](clojure.test-api.html#clojure.test/get-possibly-unbound-var)[inc-report-counter](clojure.test-api.html#clojure.test/inc-report-counter)[is](clojure.test-api.html#clojure.test/is)[join-fixtures](clojure.test-api.html#clojure.test/join-fixtures)[report](clojure.test-api.html#clojure.test/report)[run-all-tests](clojure.test-api.html#clojure.test/run-all-tests)[run-test](clojure.test-api.html#clojure.test/run-test)[run-test-var](clojure.test-api.html#clojure.test/run-test-var)[run-tests](clojure.test-api.html#clojure.test/run-tests)[set-test](clojure.test-api.html#clojure.test/set-test)[successful?](clojure.test-api.html#clojure.test/successful?)[test-all-vars](clojure.test-api.html#clojure.test/test-all-vars)[test-ns](clojure.test-api.html#clojure.test/test-ns)[test-var](clojure.test-api.html#clojure.test/test-var)[test-vars](clojure.test-api.html#clojure.test/test-vars)[testing](clojure.test-api.html#clojure.test/testing)[testing-contexts-str](clojure.test-api.html#clojure.test/testing-contexts-str)[testing-vars-str](clojure.test-api.html#clojure.test/testing-vars-str)[try-expr](clojure.test-api.html#clojure.test/try-expr)[use-fixtures](clojure.test-api.html#clojure.test/use-fixtures)[with-test](clojure.test-api.html#clojure.test/with-test)[with-test-out](clojure.test-api.html#clojure.test/with-test-out)

Variables and functions in clojure.test.junit: [with-junit-output](clojure.test-api.html#clojure.test.junit/with-junit-output)

Variables and functions in clojure.test.tap: [print-tap-diagnostic](clojure.test-api.html#clojure.test.tap/print-tap-diagnostic)[print-tap-fail](clojure.test-api.html#clojure.test.tap/print-tap-fail)[print-tap-pass](clojure.test-api.html#clojure.test.tap/print-tap-pass)[print-tap-plan](clojure.test-api.html#clojure.test.tap/print-tap-plan)[with-tap-output](clojure.test-api.html#clojure.test.tap/with-tap-output)

## clojure.tools.deps.interop

[Detailed API documentation](clojure.tools.deps.interop-api.html)

```
Functions for invoking Java processes and invoking tools via the Clojure CLI.
```

 Contents: [invoke-tool](clojure.tools.deps.interop-api.html#clojure.tools.deps.interop/invoke-tool)

## clojure.walk

by Stuart Sierra
[Detailed API documentation](clojure.walk-api.html)

```
This file defines a generic tree walker for Clojure data
structures.  It takes any data structure (list, vector, map, set,
seq), calls a function on every element, and uses the return value
of the function in place of the original.  This makes it fairly
easy to write recursive search-and-replace functions, as shown in
the examples.

Note: "walk" supports all Clojure data structures EXCEPT maps
created with sorted-map-by.  There is no (obvious) way to retrieve
the sorting function.
```

 Contents: [keywordize-keys](clojure.walk-api.html#clojure.walk/keywordize-keys)[macroexpand-all](clojure.walk-api.html#clojure.walk/macroexpand-all)[postwalk](clojure.walk-api.html#clojure.walk/postwalk)[postwalk-demo](clojure.walk-api.html#clojure.walk/postwalk-demo)[postwalk-replace](clojure.walk-api.html#clojure.walk/postwalk-replace)[prewalk](clojure.walk-api.html#clojure.walk/prewalk)[prewalk-demo](clojure.walk-api.html#clojure.walk/prewalk-demo)[prewalk-replace](clojure.walk-api.html#clojure.walk/prewalk-replace)[stringify-keys](clojure.walk-api.html#clojure.walk/stringify-keys)[walk](clojure.walk-api.html#clojure.walk/walk)

## clojure.xml

by Rich Hickey
[Detailed API documentation](clojure.xml-api.html)

```
XML reading/writing.
```

 Contents: [disable-external-entities](clojure.xml-api.html#clojure.xml/disable-external-entities)[parse](clojure.xml-api.html#clojure.xml/parse)[sax-parser](clojure.xml-api.html#clojure.xml/sax-parser)[startparse-sax](clojure.xml-api.html#clojure.xml/startparse-sax)[startparse-sax-safe](clojure.xml-api.html#clojure.xml/startparse-sax-safe)

## clojure.zip

by Rich Hickey
[Detailed API documentation](clojure.zip-api.html)

```
Functional hierarchical zipper, with navigation, editing,
and enumeration.  See Huet
```

 Contents: [append-child](clojure.zip-api.html#clojure.zip/append-child)[branch?](clojure.zip-api.html#clojure.zip/branch?)[children](clojure.zip-api.html#clojure.zip/children)[down](clojure.zip-api.html#clojure.zip/down)[edit](clojure.zip-api.html#clojure.zip/edit)[end?](clojure.zip-api.html#clojure.zip/end?)[insert-child](clojure.zip-api.html#clojure.zip/insert-child)[insert-left](clojure.zip-api.html#clojure.zip/insert-left)[insert-right](clojure.zip-api.html#clojure.zip/insert-right)[left](clojure.zip-api.html#clojure.zip/left)[leftmost](clojure.zip-api.html#clojure.zip/leftmost)[lefts](clojure.zip-api.html#clojure.zip/lefts)[make-node](clojure.zip-api.html#clojure.zip/make-node)[next](clojure.zip-api.html#clojure.zip/next)[node](clojure.zip-api.html#clojure.zip/node)[path](clojure.zip-api.html#clojure.zip/path)[prev](clojure.zip-api.html#clojure.zip/prev)[remove](clojure.zip-api.html#clojure.zip/remove)[replace](clojure.zip-api.html#clojure.zip/replace)[right](clojure.zip-api.html#clojure.zip/right)[rightmost](clojure.zip-api.html#clojure.zip/rightmost)[rights](clojure.zip-api.html#clojure.zip/rights)[root](clojure.zip-api.html#clojure.zip/root)[seq-zip](clojure.zip-api.html#clojure.zip/seq-zip)[up](clojure.zip-api.html#clojure.zip/up)[vector-zip](clojure.zip-api.html#clojure.zip/vector-zip)[xml-zip](clojure.zip-api.html#clojure.zip/xml-zip)[zipper](clojure.zip-api.html#clojure.zip/zipper)
Copyright 2007-2025 by Rich HickeyLogo & site design by [Tom Hickey](http://www.tomhickey.com).
 Clojure auto-documentation system by Tom Faulhaber.
