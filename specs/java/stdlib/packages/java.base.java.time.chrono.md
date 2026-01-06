Module[java.base](../../../module-summary.html)

# Package java.time.chrono

package java.time.chrono

 Generic API for calendar systems other than the default ISO. 

 The main API is based around the calendar system defined in ISO-8601. However, there are other calendar systems, and this package provides basic support for them. The alternate calendars are provided in the [java.time.chrono](package-summary.html) package. 

 A calendar system is defined by the [Chronology](Chronology.html) interface, while a date in a calendar system is defined by the [ChronoLocalDate](ChronoLocalDate.html) interface. 

 It is intended that applications use the main API whenever possible, including code to read and write from a persistent data store, such as a database, and to send dates and times across a network. The "chrono" classes are then used at the user interface level to deal with localized input/output. See [ChronoLocalDate](ChronoLocalDate.html) for a full discussion of the issues. 

 Using non-ISO calendar systems in an application introduces significant extra complexity. Ensure that the warnings and recommendations in `ChronoLocalDate` have been read before working with the "chrono" interfaces. 

 The supported calendar systems includes: 

- [Hijrah calendar](HijrahChronology.html)
- [Japanese calendar](JapaneseChronology.html)
- [Minguo calendar](MinguoChronology.html)
- [Thai Buddhist calendar](ThaiBuddhistChronology.html)

## Example

 This example lists today's date for all of the available calendars. 

```

   // Enumerate the list of available calendars and print today's date for each.
       Set<Chronology> chronos = Chronology.getAvailableChronologies();
       for (Chronology chrono : chronos) {
           ChronoLocalDate date = chrono.dateNow();
           System.out.printf("   %20s: %s%n", chrono.getId(), date.toString());
       }
 
```

 This example creates and uses a date in a named non-ISO calendar system. 

```

   // Print the Thai Buddhist date
       ChronoLocalDate now1 = Chronology.of("ThaiBuddhist").dateNow();
       int day = now1.get(ChronoField.DAY_OF_MONTH);
       int dow = now1.get(ChronoField.DAY_OF_WEEK);
       int month = now1.get(ChronoField.MONTH_OF_YEAR);
       int year = now1.get(ChronoField.YEAR);
       System.out.printf("  Today is %s %s %d-%s-%d%n", now1.getChronology().getId(),
                 dow, day, month, year);
   // Print today's date and the last day of the year for the Thai Buddhist Calendar.
       ChronoLocalDate first = now1
                 .with(ChronoField.DAY_OF_MONTH, 1)
                 .with(ChronoField.MONTH_OF_YEAR, 1);
       ChronoLocalDate last = first
                 .plus(1, ChronoUnit.YEARS)
                 .minus(1, ChronoUnit.DAYS);
       System.out.printf("  %s: 1st of year: %s; end of year: %s%n", last.getChronology().getId(),
                 first, last);
  
```

 This example creates and uses a date in a specific ThaiBuddhist calendar system. 

```

   // Print the Thai Buddhist date
       ThaiBuddhistDate now1 = ThaiBuddhistDate.now();
       int day = now1.get(ChronoField.DAY_OF_MONTH);
       int dow = now1.get(ChronoField.DAY_OF_WEEK);
       int month = now1.get(ChronoField.MONTH_OF_YEAR);
       int year = now1.get(ChronoField.YEAR);
       System.out.printf("  Today is %s %s %d-%s-%d%n", now1.getChronology().getId(),
                 dow, day, month, year);

   // Print today's date and the last day of the year for the Thai Buddhist Calendar.
       ThaiBuddhistDate first = now1
                 .with(ChronoField.DAY_OF_MONTH, 1)
                 .with(ChronoField.MONTH_OF_YEAR, 1);
       ThaiBuddhistDate last = first
                 .plus(1, ChronoUnit.YEARS)
                 .minus(1, ChronoUnit.DAYS);
       System.out.printf("  %s: 1st of year: %s; end of year: %s%n", last.getChronology().getId(),
                 first, last);
  
```

## Package specification

 Unless otherwise noted, passing a null argument to a constructor or method in any class or interface in this package will cause a [NullPointerException](../../lang/NullPointerException.html) to be thrown. The Javadoc "@param" definition is used to summarise the null-behavior. The "@throws [NullPointerException](../../lang/NullPointerException.html)" is not explicitly documented in each method. 

 All calculations should check for numeric overflow and throw either an [ArithmeticException](../../lang/ArithmeticException.html) or a [DateTimeException](../DateTimeException.html). 

Since:1.8

- Related PackagesPackageDescription[java.time](../package-summary.html) The main API for dates, times, instants, and durations.[java.time.format](../format/package-summary.html) Provides classes to print and parse dates and times.[java.time.temporal](../temporal/package-summary.html) Access to date and time using fields and units, and date time adjusters.[java.time.zone](../zone/package-summary.html) Support for time-zones and their rules.
- All Classes and InterfacesInterfacesClassesEnum ClassesClassDescription[AbstractChronology](AbstractChronology.html)An abstract implementation of a calendar system, used to organize and identify dates.[ChronoLocalDate](ChronoLocalDate.html)A date without time-of-day or time-zone in an arbitrary chronology, intended for advanced globalization use cases.[ChronoLocalDateTime](ChronoLocalDateTime.html)<D extends [ChronoLocalDate](ChronoLocalDate.html)>A date-time without a time-zone in an arbitrary chronology, intended for advanced globalization use cases.[Chronology](Chronology.html)A calendar system, used to organize and identify dates.[ChronoPeriod](ChronoPeriod.html)A date-based amount of time, such as '3 years, 4 months and 5 days' in an arbitrary chronology, intended for advanced globalization use cases.[ChronoZonedDateTime](ChronoZonedDateTime.html)<D extends [ChronoLocalDate](ChronoLocalDate.html)>A date-time with a time-zone in an arbitrary chronology, intended for advanced globalization use cases.[Era](Era.html)An era of the time-line.[HijrahChronology](HijrahChronology.html)The Hijrah calendar is a lunar calendar supporting Islamic calendars.[HijrahDate](HijrahDate.html)A date in the Hijrah calendar system.[HijrahEra](HijrahEra.html)An era in the Hijrah calendar system.[IsoChronology](IsoChronology.html)The ISO calendar system.[IsoEra](IsoEra.html)An era in the ISO calendar system.[JapaneseChronology](JapaneseChronology.html)The Japanese Imperial calendar system.[JapaneseDate](JapaneseDate.html)A date in the Japanese Imperial calendar system.[JapaneseEra](JapaneseEra.html)An era in the Japanese Imperial calendar system.[MinguoChronology](MinguoChronology.html)The Minguo calendar system.[MinguoDate](MinguoDate.html)A date in the Minguo calendar system.[MinguoEra](MinguoEra.html)An era in the Minguo calendar system.[ThaiBuddhistChronology](ThaiBuddhistChronology.html)The Thai Buddhist calendar system.[ThaiBuddhistDate](ThaiBuddhistDate.html)A date in the Thai Buddhist calendar system.[ThaiBuddhistEra](ThaiBuddhistEra.html)An era in the Thai Buddhist calendar system.
