On this page

## Memory management and native integration[​](#memory-management-and-native-integration "Direct link to Memory management and native integration")

QuestDB leverages both memory mapping and explicit memory management techniques, and integrates native code for performance-critical tasks.

### Memory-mapped files[​](#memory-mapped-files "Direct link to Memory-mapped files")

* **Direct OS integration:**
  Memory-mapped files let QuestDB use the operating system's page cache. This reduces explicit
  I/O calls and speeds up sequential reads.
* **Sequential access:**
  When data partitions by incremental timestamp, memory mapping ensures that reads are
  sequential and efficient.

### Direct memory management and native integration[​](#direct-memory-management-and-native-integration "Direct link to Direct memory management and native integration")

* **Off-heap memory usage:**
  QuestDB allocates direct memory via memory mapping and low-level APIs (such as Unsafe) to
  bypass the JVM garbage collector. This reduces latency spikes and garbage collection delays.
* **Hotpath efficiency:**
  The system pre-allocates and reuses memory in critical code paths, avoiding dynamic allocation
  on the hotpath.
* **Native code integration:**
  QuestDB uses native libraries written in C++ and Rust for performance-critical tasks. These
  native components share off-heap buffers with Java via JNI.

  + **Zero-copy interoperability:**
    Sharing memory between Java and native code minimizes data copying and reduces latency.
  + **Hybrid architecture:**
    This integration lets QuestDB use Java for rapid development and C++/Rust for low-level,
    high-performance routines.

## Next up[​](#next-up "Direct link to Next up")

Continue to [Query Engine](/docs/architecture/query-engine/) to learn how QuestDB parses, optimizes, and executes SQL queries.