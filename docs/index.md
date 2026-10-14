# Index

Source: PDF pages 444–462. Reference only; excluded from the LMS. Printed references point into the original book.

## PDF page 444

```text
                                                                   Index

## detection, 237–238                         affinity, 84
++ (pre- or post-increment) operator,         Agile Software Development: Principles,
          325, 326                                      Patterns, Practices (PPP), 15
                                              algorithms
                                                   correcting, 269–270
                    A                              repeating, 48
aborted computation, 109                           understanding, 297–298
abstract classes, 149, 271, 290               ambiguities
ABSTRACT FACTORY pattern, 38, 156,                 in code, 301
          273, 274                                 ignored tests as, 313
abstract interfaces, 94                       amplification comments, 59
abstract methods                              analysis functions, 265
     adding to ArgumentMarshaler, 234–235     “annotation form”, of AspectJ, 166
     modifying, 282                           Ant project, 76, 77
abstract terms, 95                            AOP (aspect-oriented programming),
abstraction                                             160, 163
     classes depending on, 150                APIs. See also public APIs
     code at wrong level of, 290–291               calling a null-returning method
     descending one level at a time, 37                 from, 110
     functions descending only one level           specialized for tests, 127
          of, 304–306                              wrapping third-party, 108
     mixing levels of, 36–37                  applications
     names at the appropriate level of, 311        decoupled from Spring, 164
     separating levels of, 305                     decoupling from construction
     wrapping an implementation, 11                     details, 156
abstraction levels                                 infrastructure of, 163
     raising, 290                                  keeping concurrency-related code
     separating, 305                                    separate, 181
accessor functions, Law of Demeter            arbitrary structure, 303–304
          and, 98                             args array, converting into a list, 231–232
accessors, naming, 25                         Args class
Active Records, 101                                constructing, 194
adapted server, 185                                implementation of, 194–200
                                                   rough drafts of, 201–212, 226–231


                                                                                     413
```

## PDF page 445

```text
414                                                                         Index


ArgsException class                           example, 71–72
     listing, 198–200                         experience of cleaning, 250
     merging exceptions into, 239–242         not making up for, 55
argument(s)                               bad comments, 59–74
     flag, 41                             banner, gathering functions beneath, 67
     for a function, 40                   base classes, 290, 291
     in functions, 288                    BDUF (Big Design Up Front), 167
     monadic forms of, 41                 beans, private variables manipulated,
     reducing, 43                                  100–101
argument lists, 43                        Beck, Kent, 3, 34, 71, 171, 252,
argument objects, 43                               289, 296
argument types                            behaviors, 288–289
     adding, 200, 237                     Big Design Up Front (BDUF), 167
     negative impact of, 208              blank lines, in code, 78–79
ArgumentMarshaler class                   blocks, calling functions within, 35
     adding the skeleton of, 213–214      Booch,Grady, 8–9
     birth of, 212                        boolean, passing into a function, 41
ArgumentMarshaler interface, 197–198      boolean arguments, 194, 288
arrays, moving, 279                       boolean map, deleting, 224
art, of clean code, 6–7                   boolean output, of tests, 132
artificial coupling, 293                  bound resources, 183, 184
AspectJ language, 166                     boundaries
aspect-oriented programming (AOP),            clean, 120
           160, 163                           exploring and learning, 116
aspects                                       incorrect behavior at, 289
     in AOP, 160–161                          separating known from unknown,
     “first-class” support for, 166                118–119
assert statements, 130–131                boundary condition errors, 269
assertEquals, 42                          boundary conditions
assertions, using a set of, 111               encapsulating, 304
assignments, unaligned, 87–88                 testing, 314
atomic operation, 323–324                 boundary tests, easing a migration, 118
attributes, 68                            “Bowling Game”, 312
authors                                   Boy Scout Rule, 14–15, 257
     of JUnit, 252                            following, 284
     programmers as, 13–14                    satisfying, 265
authorship statements, 55                 broken windows metaphor, 8
automated code instrumentation, 189–190   bucket brigade, 303
automated suite, of unit tests, 124       BUILD-OPERATE-CHECK pattern, 127
                                          builds, 287
                                          business logic, separating from error
                      B                            handling, 109
bad code, 3–4. See also dirty code;       bylines, 68
        messy code                        byte-manipulation libraries, 161,
    degrading effect of, 250                       162–163
```

## PDF page 446

```text
Index                                                                             415


                    C                      clean boundaries, 120
                                           clean code
The C++ Programming Language, 7                 art of, 6–7
calculations, breaking into intermediate        described, 7–12
          values, 296                           writing, 6–7
call stack, 324                            clean tests, 124–127
Callable interface, 326                    cleanliness
caller, cluttering, 104                         acquired sense of, 6–7
calling hierarchy, 106                          tied to tests, 9
calls, avoiding chains of, 98              cleanup, of code, 14–15
caring, for code, 10                       clever names, 26
Cartesian points, 42                       client, using two methods, 330
CAS operation, as atomic, 328              client code, connecting to a server, 318
change(s)                                  client-based locking, 185, 329, 330–332
     isolating from, 149–150               clientScheduler, 320
     large number of very tiny, 213        client/server application, concurrency in,
     organizing for, 147–150                         317–321
     tests enabling, 124                   Client/Server nonthreaded, code for,
change history, deleting, 270                        343–346
check exceptions, in Java, 106             client-server using threads, code changes,
circular wait, 337, 338–339                          346–347
clarification, comments as, 57             ClientTest.java, 318, 344–346
clarity, 25, 26                            closing braces, comments on, 67–68
class names, 25                            Clover, 268, 269
classes                                    clutter
     cohesion of, 140–141                       Javadocs as, 276
     creating for bigger concepts, 28–29        keeping free of, 293
     declaring instance variables, 81      code, 2
     enforcing design and business              bad, 3–4
          rules, 115                            Beck's rules of, 10
     exposing internals of, 294                 commented-out, 68–69, 287
     instrumenting into ConTest, 342            dead, 292
     keeping small, 136, 175                    explaining yourself in, 55
     minimizing the number of, 176              expressing yourself in, 54
     naming, 25, 138                            formatting of, 76
     nonthread-safe, 328–329                    implicity of, 18–19
     as nouns of a language, 49                 instrumenting, 188, 342
     organization of, 136                       jiggling, 190
     organizing to reduce risk of               making readable, 311
          change, 147                           necessity of, 2
     supporting advanced concurrency            reading from top to bottom, 37
          design, 183                           simplicity of, 18, 19
classification, of errors, 107                  technique for shrouding, 20
```

## PDF page 447

```text
416                                                                           Index


code, continued                                  redundant, 60–62, 272, 275, 286–287
    third-party, 114–115                         restating the obvious, 64
    width of lines in, 85–90                     separated from code, 54
    at wrong level of abstraction, 290–291       TODO, 58–59
code bases, dominated by error                   too much information in, 70
         handling, 103                           venting in, 65
code changes, comments not always                writing, 287
         following, 54                       “communication gap”, minimizing, 168
code completion, automatic, 20               Compare and Swap (CAS) operation,
code coverage analysis, 254–256                       327–328
code instrumentation, 188–190                ComparisonCompactor module, 252–265
“code sense”, 6, 7                               defactored, 256–261
code smells, listing of, 285–314                 final, 263–265
coding standard, 299                             interim, 261–263
cohesion                                         original code, 254–256
    of classes, 140–141                      compiler warnings, turning off, 289
    maintaining, 141–146                     complex code, demonstrating failures
command line arguments, 193–194                       in, 341
commands, separating from queries, 45–46     complexity, managing, 139–140
comment header standard, 55–56               computer science (CS) terms, using for
comment headers, replacing, 70                        names, 27
commented-out code, 68–69, 287               concepts
commenting style, example of bad, 71–72          keeping close to each other, 80
comments                                         naming, 19
    amplifying importance of                     one word per, 26
         something, 59                           separating at different levels, 290
    bad, 59–74                                   spelling similar similarly, 20
    deleting, 282                                vertical openness between, 78–79
    as failures, 54                          conceptual affinity, of code, 84
    good, 55–59                              concerns
    heuristics on, 286–287                       cross-cutting, 160–161
    HTML, 69                                     separating, 154, 166, 178, 250
    inaccurate, 54                           concrete classes, 149
    informative, 56                          concrete details, 149
    journal, 63–64                           concrete terms, 94
    legal, 55–56                             concurrency
    mandated, 63                                 defense principles, 180–182
    misleading, 63                               issues, 190
    mumbling, 59–60                              motives for adopting, 178–179
    as a necessary evil, 53–59                   myths and misconceptions about,
    noise, 64–66                                      179–180
    not making up for bad code, 55           concurrency code
    obsolete, 286                                compared to nonconcurrency-related
    poorly written, 287                               code, 181
    proper use of, 54                            focusing, 321
```

## PDF page 448

```text
Index                                                                                 417


concurrent algorithms, 179                   continuous readers, 184
concurrent applications, partition           control variables, within loop statements,
         behavior, 183                                 80–81
concurrent code                              convenient idioms, 155
    breaking, 329–333                        convention(s)
    defending from problems of, 180               following standard, 299–300
    flaws hiding in, 188                          over configuration, 164
concurrent programming, 180                       structure over, 301
Concurrent Programming in Java: Design            using consistent, 259
         Principles and Patterns, 182, 342   convoluted code, 175
concurrent programs, 178                     copyright statements, 55
concurrent update problems, 341              cosmic-rays. See one-offs
ConcurrentHashMap implementation, 183        CountDownLatch class, 183
conditionals                                 coupling. See also decoupling; temporal
    avoiding negative, 302                             coupling; tight coupling
    encapsulating, 257–258, 301                   artificial, 293
configurable data, 306                            hidden temporal, 302–303
configuration constants, 306                      lack of, 150
consequences, warning of, 58                 coverage patterns, testing, 314
consistency                                  coverage tools, 313
    in code, 292                             “crisp abstraction”, 8–9
    of enums, 278                            cross-cutting concerns, 160
    in names, 40                             Cunningham, Ward, 11–12
consistent conventions, 259                  cuteness, in code, 26
constants
    versus enums, 308–309
    hiding, 308                                                   D
    inheriting, 271, 307–308                 dangling false argument, 294
    keeping at the appropriate level, 83     data
    leaving as raw numbers, 300                   abstraction, 93–95
    not inheriting, 307–308                       copies of, 181–182
    passing as symbols, 276                       encapsulation, 181
    turning into enums, 275–276                   limiting the scope of, 181
construction                                      sets processed in parallel, 179
    moving all to main, 155, 156                  types, 97, 101
    separating with factory, 156             data structures. See also structure(s)
    of a system, 154                              compared to objects, 95, 97
constructor arguments, 157                        defined, 95
constructors, overloading, 25                     interfaces representing, 94
consumer threads, 184                             treating Active Records as, 101
ConTest tool, 190, 342                       data transfer-objects (DTOs),
context                                                100–101, 160
    adding meaningful, 27–29                 database normal forms, 48
    not adding gratuitous, 29–30             DateInterval enum, 282–283
    providing with exceptions, 107           DAY enumeration, 277
```

## PDF page 449

```text
418                                                                         Index


DayDate class, running SerialDate        description
         as, 271                              of a class, 138
DayDateFactory, 273–274                       overloading the structure of code
dead code, 288, 292                                into, 310
dead functions, 288                      descriptive names
deadlock, 183, 335–339                        choosing, 309–310
deadly embrace. See circular wait             using, 39–40
debugging, finding deadlocks, 336        design(s)
decision making, optimizing, 167–168          of concurrent algorithms, 179
decisions, postponing, 168                    minimally coupled, 167
declarations, unaligned, 87–88                principles of, 15
DECORATOR objects, 164                   design patterns, 290
DECORATOR pattern, 274                   details, paying attention to, 8
decoupled architecture, 167              DI (Dependency Injection), 157
decoupling, from construction            Dijkstra, Edsger, 48
         details, 156                    dining philosophers execution model,
decoupling strategy, concurrency                   184–185
         as, 178                         DIP (Dependency Inversion Principle),
default constructor, deleting, 276                 15, 150
degradation, preventing, 14              dirty code. See also bad code;
deletions, as the majority of                      messy code
         changes, 250                    dirty code, cleaning, 200
density, vertical in code, 79–80         dirty tests, 123
dependencies                             disinformation, avoiding, 19–20
    finding and breaking, 250            distance, vertical in code, 80–84
    injecting, 157                       distinctions, making meaningful, 20–21
    logical, 282                         domain-specific languages (DSLs),
    making logical physical, 298–299               168–169
    between methods, 329–333             domain-specific testing language, 127
    between synchronized                 DoubleArgumentMarshaler class, 238
         methods, 185                    DRY principle (Don't Repeat Yourself),
Dependency Injection (DI), 157                     181, 289
Dependency Inversion Principle (DIP),    DTOs (data transfer objects), 100–101, 160
         15, 150                         dummy scopes, 90
dependency magnet, 47                    duplicate if statements, 276
dependent functions, formatting, 82–83   duplication
derivatives                                   of code, 48
    base classes depending on, 291            in code, 289–290
    base classes knowing about, 273           eliminating, 173–175
    of the exception class, 48                focusing on, 10
    moving set functions into, 232,           forms of, 173, 290
         233–235                              reduction of, 48
    pushing functionality into, 217           strategies for eliminating, 48
```

## PDF page 450

```text
Index                                                                                 419


dyadic argument, 40                           error messages, 107, 250
dyadic functions, 42                          error processing, testing, 238–239
dynamic proxies, 161                          errorMessage method, 250
                                              errors. See also boundary condition errors;
                                                        spelling errors; string comparison
                    E                                   errors
e, as a variable name, 22                               classifying, 107
Eclipse, 26                                   Evans, Eric, 311
edit sessions, playing back, 13–14            events, 41
efficiency, of code, 7                        exception classification, 107
EJB architecture, early as over-engineered,   exception clauses, 107–108
          167                                 exception management code, 223
EJB standard, complete overhaul of, 164       exceptions
EJB2 beans, 160                                    instead of return codes, 103–105
EJB3, Bank object rewritten in, 165–166            narrowing the type of, 105–106
“elegant” code, 7                                  preferring to error codes, 46
emergent design, 171–176                           providing context with, 107
encapsulation, 136                                 separating from Args, 242–250
     of boundary conditions, 304                   throwing, 104–105, 194
     breaking, 106–107                             unchecked, 106–107
     of conditionals, 301                     execution, possible paths of, 321–326
encodings, avoiding, 23–24, 312–313           execution models, 183–185
entity bean, 158–160                          Executor framework, 326–327
enum(s)                                       ExecutorClientScheduler.java, 321
     changing MonthConstants to, 272          explanation, of intent, 56–57
     using, 308–309                           explanatory variables, 296–297
enumeration, moving, 277                      explicitness, of code, 19
environment, heuristics on, 287               expressive code, 295
environment control system, 128–129           expressiveness
envying, the scope of a class, 293                 in code, 10–11
error check, hiding a side effect, 258             ensuring, 175–176
Error class, 47–48                            Extract Method refactoring, 11
error code constants, 198–200                 Extreme Programming Adventures
error codes                                             in C#, 10
     implying a class or enum, 47–48          Extreme Programming Installed, 10
     preferring exceptions to, 46             “eye-full”, code fitting into, 79–80
     returning, 103–104
     reusing old, 48                                               F
     separating from the Args module,
          242–250                             factories, 155–156
error detection, pushing to the edges, 109    factory classes, 273–275
error flags, 103–104                          failure
error handling, 8, 47–48                           to express ourselves in code, 54
```

## PDF page 451

```text
420                                                                         Index


failure, continued                           descending one level of abstraction,
      patterns of, 314                            304–306
      tolerating with no harm, 330           doing one thing, 35–36, 302
false argument, 294                          dyadic, 42
fast tests, 132                              eliminating extraneous if statements,
fast-running threads, starving longer             262
            running, 183                     establishing the temporal nature
fear, of renaming, 30                             of, 260
Feathers, Michael, 10                        formatting dependent, 82–83
feature envy                                 gathering beneath a banner, 67
      eliminating, 293–294                   heuristics on, 288
      smelling of, 278                       intention-revealing, 19
file size, in Java, 76                       keeping small, 175
final keywords, 276                          length of, 34–35
F.I.R.S.T. acronym, 132–133                  moving, 279
First Law, of TDD, 122                       naming, 39, 297
FitNesse project                             number of arguments in, 288
      coding style for, 90                   one level of abstraction per, 36–37
      file sizes, 76, 77                     in place of comments, 67
      function in, 32–33                     renaming for clarity, 258
      invoking all tests, 224                rewriting for clarity, 258–259
flag arguments, 41, 288                      sections within, 36
focussed code, 8                             small as better, 34
foreign code. See third-party code           structured programming with, 49
formatting                                   understanding, 297–298
      horizontal, 85–90                      as verbs of a language, 49
      purpose of, 76                         writing, 49
      Uncle Bob’s rules, 90–92          futures, 326
      vertical, 76–85
formatting style, for a team of
            developers, 90                                  G
Fortran, forcing encodings, 23
                                        Gamma, Eric, 252
Fowler, Martin, 285, 293
                                        general heuristics, 288–307
frame, 324
                                        generated byte-code, 180
function arguments, 40–45
                                        generics, improving code readability, 115
function call dependencies, 84–85
                                        get functions, 218
function headers, 70
                                        getBoolean function, 224
function signature, 45
                                        GETFIELD instruction, 325, 326
functionality, placement of, 295–296
                                        getNextId method, 326
functions
                                        getState function, 129
      breaking into smaller, 141–146
      calling within a block, 35        Gilbert, David, 267, 268
      dead, 288                         given-when-then convention, 130
      defining private, 292             glitches. See one-offs
```

## PDF page 452

```text
Index                                                                        421


global setup strategy, 155                    exposing, 94
“God class”, 136–137                          hiding, 94
good comments, 55–59                          wrapping an abstraction, 11
goto statements, avoiding, 48, 49        Implementation Patterns, 3, 296
grand redesign, 5                        implicity, of code, 18
gratuitous context, 29–30                import lists
                                              avoiding long, 307
                                              shortening in SerialDate, 270
                   H                     imports, as hard dependencies, 307
hand-coded instrumentation, 189          imprecision, in code, 301
HashTable, 328–329
                                         inaccurate comments, 54
headers. See comment headers; function   inappropriate information, in
           headers                                 comments, 286
heuristics                               inappropriate static methods, 296
                                         include method, 48
     cross references of, 286, 409
                                         inconsistency, in code, 292
     general, 288–307
                                         inconsistent spellings, 20
     listing of, 285–314
                                         incrementalism, 212–214
hidden temporal coupling, 259, 302–303
                                         indent level, of a function, 35
hidden things, in a function, 44
                                         indentation, of code, 88–89
hiding
                                         indentation rules, 89
     implementation, 94
                                         independent tests, 132
     structures, 99
                                         information
hierarchy of scopes, 88
                                              inappropriate, 286
HN. See Hungarian Notation
                                              too much, 70, 291–292
horizontal alignment, of code, 87–88
                                         informative comments, 56
horizontal formatting, 85–90
                                         inheritance hierarchy, 308
horizontal white space, 86
                                         inobvious connection, between a comment
HTML, in source code, 69
                                                   and code, 70
Hungarian Notation (HN), 23–24, 295
                                         input arguments, 41
Hunt, Andy, 8, 289
                                         instance variables
hybrid structures, 99
                                              in classes, 140
                                              declaring, 81
                    I                         hiding the declaration of, 81–82
                                              passing as function
if statements                                      arguments, 231
    duplicate, 276                            proliferation of, 140
    eliminating, 262                     instrumented classes, 342
if-else chain                            insufficient tests, 313
    appearing again and again, 290       integer argument(s)
    eliminating, 233                          defining, 194
ignored tests, 313                            integrating, 224–225
implementation                           integer argument functionality,
    duplication of, 173                            moving into ArgumentMarshaler,
    encoding, 24                                   215–216
```

## PDF page 453

```text
422                                                                                Index


integer argument type, adding                Java programmers, encoding not
           to Args, 212                                needed, 24
integers, pattern of changes for, 220        Java proxies, 161–163
IntelliJ, 26                                 Java source files, 76–77
intent                                       javadocs
     explaining in code, 55                       as clutter, 276
     explanation of, 56–57                        in nonpublic code, 71
     obscured, 295                                preserving formatting in, 270
intention-revealing function, 19                  in public APIs, 59
intention-revealing names, 18–19                  requiring for every function, 63
interface(s)                                 java.util.concurrent package, collections
     defining local or remote, 158–160                 in, 182–183
     encoding, 24                            JBoss AOP, proxies in, 163
     implementing, 149–150                   JCommon library, 267
     representing abstract concerns, 150     JCommon unit tests, 270
     turning ArgumentMarshaler into, 237     JDepend project, 76, 77
     well-defined, 291–292                   JDK proxy, providing persistence support,
     writing, 119                                      161–163
internal structures, objects hiding, 97      Jeffries, Ron, 10–11, 289
intersection, of domains, 160                jiggling strategies, 190
intuition, not relying on, 289               JNDI lookups, 157
inventor of C++, 7                           journal comments, 63–64
Inversion of Control (IoC), 157              JUnit, 34
InvocationHandler object, 162                JUnit framework, 252–265
I/O bound, 318                               Junit project, 76, 77
isolating, from change, 149–150              Just-In-Time Compiler, 180
isxxxArg methods, 221–222
iterative process, refactoring as, 265
                                                                K
                     J                       keyword form, of a function name, 43

jar files, deploying derivatives and bases
           in, 291                                               L
Java
                                             L, lower-case in variable names, 20
      aspects or aspect-like mechanisms,
                                             language design, art of programming as, 49
           161–166
                                             languages
      heuristics on, 307–309
                                                  appearing to be simple, 12
      as a wordy language, 200
                                                  level of abstraction, 2
Java 5, improvements for concurrent
                                                  multiple in one source file, 288
           development, 182–183
                                                  multiples in a comment, 270
Java 5 Executor framework, 320–321
                                             last-in, first-out (LIFO) data structure,
Java 5 VM, nonblocking solutions in,
           327–328                                      operand stack as, 324
Java AOP frameworks, 163–166                 Law of Demeter, 97–98, 306
```

## PDF page 454

```text
Index                                                                                 423


LAZY INITIALIZATION/                          managers, role of, 6
           EVALUATION idiom, 154              mandated comments, 63
LAZY-INITIALIZATION, 157                      manual control, over a serial ID, 272
Lea, Doug, 182, 342                           Map
learning tests, 116, 118                          adding for ArgumentMarshaler, 221
LeBlanc’s law, 4                                  methods of, 114
legacy code, 307                              maps, breaking the use of, 222–223
legal comments, 55–56                         marshalling implementation,
level of abstraction, 36–37                            214–215
levels of detail, 99                          meaningful context, 27–29
lexicon, having a consistent, 26              member variables
lines of code                                     f prefix for, 257
      duplicating, 173                            prefixing, 24
      width of, 85                                renaming for clarity, 259
list(s)                                       mental mapping, avoiding, 25
      of arguments, 43                        messy code. See also bad code; dirty code
      meaning specific to programmers, 19         total cost of owning, 4–12
      returning a predefined immutable, 110   method invocations, 324
literate code, 9                              method names, 25
literate programming, 9                       methods
Literate Programming, 141                         affecting the order of execution, 188
livelock, 183, 338                                calling a twin with a flag, 278
local comments, 69–70                             changing from static to instance, 280
local variables, 324                              of classes, 140
      declaring, 292                              dependencies between, 329–333
      at the top of each function, 80             eliminating duplication between,
lock & wait, 337, 338                                  173–174
locks, introducing, 185                           minimizing assert statements in, 176
log4j package, 116–118                            naming, 25
logical dependencies, 282, 298–299                tests exposing bugs in, 269
LOGO language, 36                             minimal code, 9
long descriptive names, 39                    misleading comments, 63
long names, for long scopes, 312              misplaced responsibility, 295–296, 299
loop counters, single-letter names for, 25    MOCK OBJECT, assigning, 155
                                              monadic argument, 40
                                              monadic forms, of arguments, 41
                   M                          monads, converting dyads into, 42
                                              Monte Carlo testing, 341
magic numbers                                 Month enum, 278
    obscuring intent, 295                     MonthConstants class, 271
    replacing with named constants,           multithread aware, 332
         300–301                              multithread-calculation, of throughput,
main function, moving construction to,
                                                       335
         155, 156
```

## PDF page 455

```text
424                                                                                 Index


multithreaded code, 188, 339–342               Newkirk, Jim, 116
mumbling, 59–60                                newspaper metaphor, 77–78
mutators, naming, 25                           niladic argument, 40
mutual exclusion, 183, 336, 337                no preemption, 337
                                               noise
                                                    comments, 64–66
                    N                               scary, 66
named constants, replacing magic                    words, 21
         numbers, 300–301                      nomenclature, using standard, 311–312
name-length-challenged languages, 23           nonblocking solutions, 327–328
names                                          nonconcurrency-related code, 181
    abstractions, appropriate level of, 311    noninformative names, 21
    changing, 40                               nonlocal information, 69–70
    choosing, 175, 309–310                     nonpublic code, javadocs in, 71
    of classes, 270–271                        nonstatic methods, preferred to static, 296
    clever, 26                                 nonthreaded code, getting working
    descriptive, 39–40                                   first, 187
    of functions, 297                          nonthread-safe classes, 328–329
    heuristics on, 309–313                     normal flow, 109
    importance of, 309–310                     null
    intention-revealing, 18–19                      not passing into methods, 111–112
    length of corresponding to scope,               not returning, 109–110
         22–23                                      passed by a caller accidentally, 111
    long names for long scopes, 312            null detection logic, for ArgumentMarshaler,
    making unambiguous, 258                              214
    problem domain, 27                         NullPointerException, 110, 111
    pronounceable, 21–22                       number-series naming, 21
    rules for creating, 18–30
    searchable, 22–23                                              O
    shorter generally better than longer, 30
    solution domain, 27                        Object Oriented Analysis and Design with
    with subtle differences, 20                         Applications, 8
    unambiguous, 312                           object-oriented design, 15
    at the wrong level of abstraction, 271     objects
naming, classes, 138                               compared to data structures, 95, 97
naming conventions, as inferior to                 compared to data types and proce-
         structures, 301                                dures, 101
navigational methods, in Active                    copying read-only, 181
         Records, 101                              defined, 95
near bugs, testing, 314                        obscured intent, 295
negative conditionals, avoiding, 302           obsolete comments, 286
negatives, 258                                 obvious behavior, 288–289
nested structures, 46                          obvious code, 12
```

## PDF page 456

```text
Index                                                                                425


“Once and only once” principle, 289            performance
“ONE SWITCH” rule, 299                              of a client/server pair, 318
one thing, functions doing, 35–36, 302              concurrency improving, 179
one-offs, 180, 187, 191                             of server-based locking, 333
OO code, 97                                    permutations, calculating, 323
OO design, 139                                 persistence, 160, 161
Open Closed Principle (OCP), 15, 38            pessimistic locking, 327
    by checked exceptions, 106                 phraseology, in similar names, 40
    supporting, 149                            physicalizing, a dependency, 299
operand stack, 324                             Plain-Old Java Objects. See POJOs
operating systems, threading policies, 188     platforms, running threaded code, 188
operators, precedence of, 86                   pleasing code, 7
optimistic locking, 327                        pluggable thread-based code, 187
optimizations, LAZY-EVALUATION                 POJO system, agility provided by, 168
         as, 157                               POJOs (Plain-Old Java Objects)
optimizing, decision making, 167–168                creating, 187
orderings, calculating the possible, 322–323        implementing business logic, 162
organization                                        separating threaded-aware code, 190
    for change, 147–150                             in Spring, 163
    of classes, 136                                 writing application domain logic, 166
    managing complexity, 139–140               polyadic argument, 40
outbound tests, exercising an interface, 118   polymorphic behavior, of functions, 296
output arguments, 41, 288                      polymorphic changes, 96–97
    avoiding, 45                               polymorphism, 37, 299
    need for disappearing, 45                  position markers, 67
outputs, arguments as, 45                      positives
overhead, incurred by concurrency, 179              as easier to understand, 258
overloading, of code with description, 310          expressing conditionals as, 302
                                                    of decisions, 301precision
                                                    as the point of all naming, 30
                    P                          predicates, naming, 25
paperback model, as an academic                preemption, breaking, 338
          model, 27                            prefixes
parameters, taken by instructions, 324              for member variables, 24
parse operation, throwing an                        as useless in today’s environments,
          exception, 220                                 312–313
partitioning, 250                              pre-increment operator, ++, 324, 325, 326
paths of execution, 321–326                    “prequel”, this book as, 15
pathways, through critical sections, 188       principle of least surprise, 288–289, 295
pattern names, using standard, 175             principles, of design, 15
patterns                                       PrintPrimes program, translation into
     of failure, 314                                     Java, 141
     as one kind of standard, 311              private behavior, isolating, 148–149
```

## PDF page 457

```text
426                                                                            Index


private functions, 292                           Dave Thomas on, 9
private method behavior, 147                     improving using generics, 115
problem domain names, 27                    readability perspective, 8
procedural code, 97                         readers
procedural shape example, 95–96                  of code, 13–14
procedures, compared to objects, 101             continuous, 184
process function, repartitioning, 319–320   readers-writers execution model, 184
process method, I/O bound, 319              reading
processes, competing for resources, 184          clean code, 8
processor bound, code as, 318                    code from top to bottom, 37
producer consumer execution model, 184           versus writing, 14
producer threads, 184                       reboots, as a lock up solution, 331
production environment, 127–130             recommendations, in this book, 13
productivity, decreased by messy code, 4    redesign, demanded by the team, 5
professional programmer, 25                 redundancy, of noise words, 21
professional review, of code, 268           redundant comments, 60–62, 272, 275,
programmers                                           286–287
    as authors, 13–14                       ReentrantLock class, 183
    conundrum faced by, 6                   refactored programs, as longer, 146
    responsibility for messes, 5–6          refactoring
    unprofessional, 5–6                          Args, 212
programming                                      code incrementally, 172
    defined, 2                                   as an iterative process, 265
    structured, 48–49                            putting things in to take out, 233
programs, getting them to work, 201              test code, 127
pronounceable names, 21–22                  Refactoring (Fowler), 285
protected variables, avoiding, 80           renaming, fear of, 30
proxies, drawbacks of, 163                  repeatability, of concurrency bugs, 180
public APIs, javadocs in, 59                repeatable tests, 132
puns, avoiding, 26–27                       requirements, specifying, 2
PUTFIELD instruction, as atomic, 325        resetId, byte-code generated for, 324–325
                                            resources
                                                 bound, 183
                    Q                            processes competing for, 184
queries, separating from commands, 45–46         threads agreeing on a global ordering
                                                      of, 338
                                            responsibilities
                    R                            counting in classes, 136
                                                 definition of, 138
random jiggling, tests running, 190
                                                 identifying, 139
range, including end-point dates in, 276
                                                 misplaced, 295–296, 299
readability
                                                 splitting a program into main, 146
    of clean tests, 124
                                            return codes, using exceptions instead,
    of code, 76
                                                      103–105
```

## PDF page 458

```text
Index                                                                               427


reuse, 174                                    server application, 317–318, 343–344
risk of change, reducing, 147                 server code, responsibilities of, 319
robust clear code, writing, 112               server-based locking, 329
rough drafts, writing, 200                         as preferred, 332–333
runnable interface, 326                            with synchronized methods, 185
run-on expressions, 295                       “Servlet” model, of Web applications, 178
run-on journal entries, 63–64                 Servlets, synchronization problems, 182
runtime logic, separating startup from, 154   set functions, moving into appropriate
                                                        derivatives, 232, 233–235
                                              setArgument, changing, 232–233
                    S                         setBoolean function, 217
safety mechanisms, overridden, 289            setter methods, injecting dependencies,
scaling up, 157–161                                     157
scary noise, 66                               setup strategy, 155
schema, of a class, 194                       SetupTeardownIncluder.java listing,
schools of thought, about clean code,                   50–52
          12–13                               shape classes, 95–96
scissors rule, in C++, 81                     shared data, limiting access, 181
scope(s)                                      shared variables
     defined by exceptions, 105                    method updating, 328
     dummy, 90                                     reducing the scope of, 333
     envying, 293                             shotgun approach, hand-coded instrumen-
     expanding and indenting, 89                        tation as, 189
     hierarchy in a source file, 88           shut-down code, 186
     limiting for data, 181                   shutdowns, graceful, 186
     names related to the length of,          side effects
          22–23, 312                               having none, 44
     of shared variables, 333                      names describing, 313
searchable names, 22–23                       Simmons, Robert, 276
Second Law, of TDD, 122                       simple code, 10, 12
sections, within functions, 36                Simple Design, rules of, 171–176
selector arguments, avoiding, 294–295         simplicity, of code, 18, 19
self validating tests, 132                    single assert rule, 130–131
Semaphore class, 183                          single concepts, in each test function,
semicolon, making visible, 90                           131–132
“serial number”, SerialDate using, 271        Single Responsibility Principle (SRP), 15,
SerialDate class                                        138–140
     making it right, 270–284                      applying, 321
     naming of, 270–271                            breaking, 155
     refactoring, 267–284                          as a concurrency defense principle,
SerialDateTests class, 268                              181
serialization, 272                                 recognizing violations of, 174
server, threads created by, 319–321                server violating, 320
```

## PDF page 459

```text
428                                                                           Index


Single Responsibility Principle (SRP),      starvation, 183, 184, 338
          continued                         static function, 279
     Sql class violating, 147               static import, 308
     supporting, 157                        static methods, inappropriate, 296
     in test classes conforming to, 172     The Step-down Rule, 37
     violating, 38                          stories, implementing only today’s, 158
single value, ordered components of, 42     STRATEGY pattern, 290
single-letter names, 22, 25                 string arguments, 194, 208–212, 214–225
single-thread calculation, of throughput,   string comparison errors, 252
          334                               StringBuffers, 129
SINGLETON pattern, 274                      Stroustrup, Bjarne, 7–8
small classes, 136                          structure(s). See also data structures
Smalltalk Best Practice Patterns, 296            hiding, 99
smart programmer, 25                             hybrid, 99
software project, maintenance of, 175            making massive changes to, 212
software systems. See also system(s)             over convention, 301
     compared to physical systems, 158      structured programming, 48–49
SOLID class design principle, 150           SuperDashboard class, 136–137
solution domain names, 27                   swapping, as permutations, 323
source code control systems, 64, 68, 69     switch statements
source files                                     burying, 37, 38
     compared to newspaper articles,             considering polymorphism
          77–78                                        before, 299
     multiple languages in, 288                  reasons to tolerate, 38–39
Sparkle program, 34                         switch/case chain, 290
spawned threads, deadlocked, 186            synchronization problems, avoiding with
special case objects, 110                              Servlets, 182
SPECIAL CASE PATTERN, 109                   synchronized block, 334
specifications, purpose of, 2               synchronized keyword, 185
spelling errors, correcting, 20                  adding, 323
SpreadsheetDateFactory, 274–275                  always acquiring a lock, 328
Spring AOP, proxies in, 163                      introducing a lock via, 331
Spring Framework, 157                            protecting a critical section
Spring model, following EJB3, 165                      in code, 181
Spring V2.5 configuration file, 163–164     synchronized methods, 185
spurious failures, 187                      synchronizing, avoiding, 182
Sql class, changing, 147–149                synthesis functions, 265
square root, as the iteration limit, 74     system(s). See also software systems
SRP. See Single Responsibility Principle         file sizes of significant, 77
standard conventions, 299–300                    keeping running during development,
standard nomenclature, 175, 311–312                    213
standards, using wisely, 168                     needing domain-specific, 168
startup process, separating from runtime    system architecture, test driving,
          logic, 154                                   166–167
```

## PDF page 460

```text
Index                                                                               429


system failures, not ignoring                test functions, single concepts in, 131–132
         one-offs, 187                       test implementation, of an interface, 150
system level, staying clean at, 154          test suite
system-wide information, in a local                automated, 213
         comment, 69–70                            of unit tests, 124, 268
                                                   verifying precise behavior, 146
                                             testable systems, 172
                    T                        test-driven development. See TDD
tables, moving, 275                          testing
target deployment platforms, running tests         arguments making harder, 40
          on, 341                                  construction logic mixed with
task swapping, encouraging, 188                         runtime, 155
TDD (Test Driven Development), 213           testing language, domain-specific, 127
     building logic, 106                     testNG project, 76, 77
     as fundamental discipline, 9            tests
     laws of, 122–123                              clean, 124–127
team rules, 90                                     cleanliness tied to, 9
teams                                              commented out for SerialDate,
     coding standard for every, 299–300                 268–270
     slowed by messy code, 4                       dirty, 123
technical names, choosing, 27                      enabling the -ilities, 124
technical notes, reserving comments                fast, 132
          for, 286                                 fast versus slow, 314
TEMPLATE METHOD pattern                            heuristics on, 313–314
     addressing duplication, 290                   ignored, 313
     removing higher-level duplication,            independent, 132
          174–175                                  insufficient, 313
     using, 130                                    keeping clean, 123–124
temporal coupling. See also coupling               minimizing assert statements in,
     exposing, 259–260                                  130–131
     hidden, 302–303                               not stopping trivial, 313
     side effect creating, 44                      refactoring, 126–127
temporary variables, explaining, 279–281           repeatable, 132
test cases                                         requiring more than one step, 287
     adding to check arguments, 237                running, 341
     in ComparisonCompactor, 252–254               self validating, 132
     patterns of failure, 269, 314                 simple design running all, 172
     turning off, 58                               suite of automated, 213
test code, 124, 127                                timely, 133
TEST DOUBLE, assigning, 155                        writing for multithreaded code,
Test Driven Development. See TDD                        339–342
test driving, architecture, 166–167                writing for threaded code, 186–190
test environment, 127–130                          writing good, 122–123
```

## PDF page 461

```text
430                                                                               Index


Third Law, of TDD, 122                        timer program, testing, 121–122
third-party code                              “TO” keyword, 36
     integrating, 116                         TO paragraphs, 37
     learning, 116                            TODO comments, 58–59
     using, 114–115                           tokens, used as magic numbers, 300
     writing tests for, 116                   Tomcat project, 76, 77
this variable, 324                            tools
Thomas, Dave, 8, 9, 289                            ConTest tool, 190, 342
thread(s)                                          coverage, 313
     adding to a method, 322                       handling proxy boilerplate, 163
     interfering with each other, 330              testing thread-based code, 342
     making as independent as                 train wrecks, 98–99
           possible, 182                      transformations, as return values, 41
     stepping on each other, 180, 326         transitive navigation, avoiding, 306–307
     taking resources from other              triadic argument, 40
           threads, 338                       triads, 42
thread management strategy, 320               try blocks, 105
thread pools, 326                             try/catch blocks, 46–47, 65–66
thread-based code, testing, 342               try-catch-finally statement, 105–106
threaded code                                 tunable threaded-based code, 187–188
     making pluggable, 187                    type encoding, 24
     making tunable, 187–188
     symptoms of bugs in, 187
     testing, 186–190                                             U
     writing in Java 5, 182–183               ubiquitous language, 311–312
threading                                     unambiguous names, 312
     adding to a client/server application,   unchecked exceptions, 106–107
           319, 346–347                       unencapsulated conditional, encapsulating,
     problems in complex systems, 342                   257
thread-safe collections, 182–183, 329         unit testing, isolated as difficult, 160
throughput                                    unit tests, 124, 175, 268
     causing starvation, 184                  unprofessional programming, 5–6
     improving, 319                           uppercase C, in variable names, 20
     increasing, 333–335                      usability, of newspapers, 78
     validating, 318                          use, of a system, 154
throws clause, 106                            users, handling concurrently, 179
tiger team, 5
tight coupling, 172
time, taking to go fast, 6                                        V
Time and Money project, 76
                                              validation, of throughput, 318
     file sizes, 77
                                              variable names, single-letter, 25
timely tests, 133
```

## PDF page 462

```text
Index                                                                           431


variables                                                   W
     1 based versus zero based, 261
     declaring, 80, 81, 292               wading, through bad code, 3
     explaining temporary, 279–281        Web containers, decoupling provided
     explanatory, 296–297                           by, 178
     keeping private, 93                  what, decoupling from when, 178
     local, 292, 324                      white space, use of horizontal, 86
     moving to a different class, 273     wildcards, 307
     in place of comments, 67             Working Effectively with Legacy
     promoting to instance variables of             Code, 10
          classes, 141                    “working” programs, 201
     with unclear context, 28             workmanship, 176
venting, in comments, 65                  wrappers, 108
verbs, keywords and, 43                   wrapping, 108
Version class, 139                        writers, starvation of, 184
versions, not deserializing across, 272   “Writing Shy Code”, 306
vertical density, in code, 79–80
vertical distance, in code, 80–84
vertical formatting, 76–85
                                                            X
vertical openness, between concepts,      XML
          78–79                             deployment descriptors, 160
vertical ordering, in code, 84–85           “policy” specified configuration
vertical separation, 292                        files, 164
```

