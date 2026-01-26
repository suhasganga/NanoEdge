### [Configuration Preprocessor Definitions](configuration_preprocessor_defin.html "Configuration Preprocessor Definitions")

A number of configuration preprocessor definitions can be used to change
the behavior of Beast. The user should assume that they introduce significant
changes to the public part of this library's API and make sure that all translation
units (usually files) compiled and linked into a program use the same combination
of configuration macros, failure to do so may result in violations of ODR
(One Definition Rule).

**Table 1.14. Special Fields**

| Definition | Description |
| --- | --- |
| BOOST\_BEAST\_SEPARATE\_COMPILATION | Enables the split compilation mode, which allows the user to compile definitions of non-template entities in a single translation unit, thus improving compilation speed. That translation unit has to include boost/beast/src.hpp in order to compile the definitions. |
| BOOST\_BEAST\_ALLOW\_DEPRECATED | Enables the use of deprecated APIs within Beast. |
| BOOST\_BEAST\_FILE\_BUFFER\_SIZE | Sets the small buffer size for the file\_body. Defaults to 4096. |