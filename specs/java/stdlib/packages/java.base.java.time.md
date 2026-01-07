java.time (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

- [Overview](../../../index.html)
- [Module](../../module-summary.html)
- Package
- Class
- [Use](package-use.html)
- [Tree](package-tree.html)
- [Preview](../../../preview-list.html)
- [New](../../../new-list.html)
- [Deprecated](../../../deprecated-list.html)
- [Index](../../../index-files/index-1.html)
- [Help](../../../help-doc.html#package)

- 

Package:

  - [Description](#package-description)
  - [Related Packages](#related-package-summary)
  - [Classes and Interfaces](#class-summary)

- Package: 
- [Description](#package-description) | 
- [Related Packages](#related-package-summary) | 
- [Classes and Interfaces](#class-summary)

[SEARCH](../../../search.html)Module[java.base](../../module-summary.html)

# Package java.time

package java.time

 The main API for dates, times, instants, and durations. 

 The classes defined here represent the principle date-time concepts, including instants, durations, dates, times, time-zones and periods. They are based on the ISO calendar system, which is the de facto world calendar following the proleptic Gregorian rules. All the classes are immutable and thread-safe. 

 Each date time instance is composed of fields that are conveniently made available by the APIs. For lower level access to the fields refer to the `java.time.temporal` package. Each class includes support for printing and parsing all manner of dates and times. Refer to the `java.time.format` package for customization options. 

 The `java.time.chrono` package contains the calendar neutral API [ChronoLocalDate](chrono/ChronoLocalDate.html), [ChronoLocalDateTime](chrono/ChronoLocalDateTime.html), [ChronoZonedDateTime](chrono/ChronoZonedDateTime.html) and [Era](chrono/Era.html). This is intended for use by applications that need to use localized calendars. It is recommended that applications use the ISO-8601 date and time classes from this package across system boundaries, such as to the database or across the network. The calendar neutral API should be reserved for interactions with users. 

## Dates and Times

[Instant](Instant.html) is essentially a numeric timestamp. The current Instant can be retrieved from a [Clock](Clock.html). This is useful for logging and persistence of a point in time and has in the past been associated with storing the result from [System.currentTimeMillis()](../lang/System.html#currentTimeMillis()). 

[LocalDate](LocalDate.html) stores a date without a time. This stores a date like '2010-12-03' and could be used to store a birthday. 

[LocalTime](LocalTime.html) stores a time without a date. This stores a time like '11:30' and could be used to store an opening or closing time. 

[LocalDateTime](LocalDateTime.html) stores a date and time. This stores a date-time like '2010-12-03T11:30'. 

[ZonedDateTime](ZonedDateTime.html) stores a date and time with a time-zone. This is useful if you want to perform accurate calculations of dates and times taking into account the [ZoneId](ZoneId.html), such as 'Europe/Paris'. Where possible, it is recommended to use a simpler class without a time-zone. The widespread use of time-zones tends to add considerable complexity to an application. 

## Duration and Period

 Beyond dates and times, the API also allows the storage of periods and durations of time. A [Duration](Duration.html) is a simple measure of time along the time-line in nanoseconds. A [Period](Period.html) expresses an amount of time in units meaningful to humans, such as years or days. 

## Additional value types

[Month](Month.html) stores a month on its own. This stores a single month-of-year in isolation, such as 'DECEMBER'. 

[DayOfWeek](DayOfWeek.html) stores a day-of-week on its own. This stores a single day-of-week in isolation, such as 'TUESDAY'. 

[Year](Year.html) stores a year on its own. This stores a single year in isolation, such as '2010'. 

[YearMonth](YearMonth.html) stores a year and month without a day or time. This stores a year and month, such as '2010-12' and could be used for a credit card expiry. 

[MonthDay](MonthDay.html) stores a month and day without a year or time. This stores a month and day-of-month, such as '--12-03' and could be used to store an annual event like a birthday without storing the year. 

[OffsetTime](OffsetTime.html) stores a time and offset from UTC without a date. This stores a date like '11:30+01:00'. The [ZoneOffset](ZoneOffset.html) is of the form '+01:00'. 

[OffsetDateTime](OffsetDateTime.html) stores a date and time and offset from UTC. This stores a date-time like '2010-12-03T11:30+01:00'. This is sometimes found in XML messages and other forms of persistence, but contains less information than a full time-zone. 

## Package specification

 Unless otherwise noted, passing a null argument to a constructor or method in any class or interface in this package will cause a [NullPointerException](../lang/NullPointerException.html) to be thrown. The Javadoc "@param" definition is used to summarise the null-behavior. The "@throws [NullPointerException](../lang/NullPointerException.html)" is not explicitly documented in each method. 

 All calculations should check for numeric overflow and throw either an [ArithmeticException](../lang/ArithmeticException.html) or a [DateTimeException](DateTimeException.html). 

## Design notes (non normative)

 The API has been designed to reject null early and to be clear about this behavior. A key exception is any method that takes an object and returns a boolean, for the purpose of checking or validating, will generally return false for null. 

 The API is designed to be type-safe where reasonable in the main high-level API. Thus, there are separate classes for the distinct concepts of date, time and date-time, plus variants for offset and time-zone. This can seem like a lot of classes, but most applications can begin with just five date/time types. 

- [Instant](Instant.html) - a timestamp
- [LocalDate](LocalDate.html) - a date without a time, or any reference to an offset or time-zone
- [LocalTime](LocalTime.html) - a time without a date, or any reference to an offset or time-zone
- [LocalDateTime](LocalDateTime.html) - combines date and time, but still without any offset or time-zone
- [ZonedDateTime](ZonedDateTime.html) - a "full" date-time with time-zone and resolved offset from UTC/Greenwich

`Instant` is the closest equivalent class to `java.util.Date`. `ZonedDateTime` is the closest equivalent class to `java.util.GregorianCalendar`. 

 Where possible, applications should use `LocalDate`, `LocalTime` and `LocalDateTime` to better model the domain. For example, a birthday should be stored in a code `LocalDate`. Bear in mind that any use of a [time-zone](ZoneId.html), such as 'Europe/Paris', adds considerable complexity to a calculation. Many applications can be written only using `LocalDate`, `LocalTime` and `Instant`, with the time-zone added at the user interface (UI) layer. 

 The offset-based date-time types `OffsetTime` and `OffsetDateTime`, are intended primarily for use with network protocols and database access. For example, most databases cannot automatically store a time-zone like 'Europe/Paris', but they can store an offset like '+02:00'. 

 Classes are also provided for the most important sub-parts of a date, including `Month`, `DayOfWeek`, `Year`, `YearMonth` and `MonthDay`. These can be used to model more complex date-time concepts. For example, `YearMonth` is useful for representing a credit card expiry. 

 Note that while there are a large number of classes representing different aspects of dates, there are relatively few dealing with different aspects of time. Following type-safety to its logical conclusion would have resulted in classes for hour-minute, hour-minute-second and hour-minute-second-nanosecond. While logically pure, this was not a practical option as it would have almost tripled the number of classes due to the combinations of date and time. Thus, `LocalTime` is used for all precisions of time, with zeroes used to imply lower precision. 

 Following full type-safety to its ultimate conclusion might also argue for a separate class for each field in date-time, such as a class for HourOfDay and another for DayOfMonth. This approach was tried, but was excessively complicated in the Java language, lacking usability. A similar problem occurs with periods. There is a case for a separate class for each period unit, such as a type for Years and a type for Minutes. However, this yields a lot of classes and a problem of type conversion. Thus, the set of date-time types provided is a compromise between purity and practicality. 

 The API has a relatively large surface area in terms of number of methods. This is made manageable through the use of consistent method prefixes. 

- `of` - static factory method
- `parse` - static factory method focused on parsing
- `get` - gets the value of something
- `is` - checks if something is true
- `with` - the immutable equivalent of a setter
- `plus` - adds an amount to an object
- `minus` - subtracts an amount from an object
- `to` - converts this object to another type
- `at` - combines this object with another, such as `date.atTime(time)`

 Multiple calendar systems is an awkward addition to the design challenges. The first principle is that most users want the standard ISO calendar system. As such, the main classes are ISO-only. The second principle is that most of those that want a non-ISO calendar system want it for user interaction, thus it is a UI localization issue. As such, date and time objects should be held as ISO objects in the data model and persistent storage, only being converted to and from a local calendar for display. The calendar system would be stored separately in the user preferences. 

 There are, however, some limited use cases where users believe they need to store and use dates in arbitrary calendar systems throughout the application. This is supported by [ChronoLocalDate](chrono/ChronoLocalDate.html), however it is vital to read all the associated warnings in the Javadoc of that interface before using it. In summary, applications that require general interoperation between multiple calendar systems typically need to be written in a very different way to those only using the ISO calendar, thus most applications should just use ISO and avoid `ChronoLocalDate`. 

 The API is also designed for user extensibility, as there are many ways of calculating time. The [field](temporal/TemporalField.html) and [unit](temporal/TemporalUnit.html) API, accessed via [TemporalAccessor](temporal/TemporalAccessor.html) and [Temporal](temporal/Temporal.html) provide considerable flexibility to applications. In addition, the [TemporalQuery](temporal/TemporalQuery.html) and [TemporalAdjuster](temporal/TemporalAdjuster.html) interfaces provide day-to-day power, allowing code to read close to business requirements: 

```

   LocalDate customerBirthday = customer.loadBirthdayFromDatabase();
   LocalDate today = LocalDate.now();
   if (customerBirthday.equals(today)) {
     LocalDate specialOfferExpiryDate = today.plusWeeks(2).with(next(FRIDAY));
     customer.sendBirthdaySpecialOffer(specialOfferExpiryDate);
   }

 
```

Since:1.8

- Related PackagesPackageDescription[java.time.chrono](chrono/package-summary.html) Generic API for calendar systems other than the default ISO.[java.time.format](format/package-summary.html) Provides classes to print and parse dates and times.[java.time.temporal](temporal/package-summary.html) Access to date and time using fields and units, and date time adjusters.[java.time.zone](zone/package-summary.html) Support for time-zones and their rules.
- All Classes and InterfacesInterfacesClassesEnum ClassesException ClassesClassDescription[Clock](Clock.html)A clock providing access to the current instant, date and time using a time-zone.[DateTimeException](DateTimeException.html)Exception used to indicate a problem while calculating a date-time.[DayOfWeek](DayOfWeek.html)A day-of-week, such as 'Tuesday'.[Duration](Duration.html)A time-based amount of time, such as '34.5 seconds'.[Instant](Instant.html)An instantaneous point on the time-line.[InstantSource](InstantSource.html)Provides access to the current instant.[LocalDate](LocalDate.html)A date without a time-zone in the ISO-8601 calendar system, such as `2007-12-03`.[LocalDateTime](LocalDateTime.html)A date-time without a time-zone in the ISO-8601 calendar system, such as `2007-12-03T10:15:30`.[LocalTime](LocalTime.html)A time without a time-zone in the ISO-8601 calendar system, such as `10:15:30`.[Month](Month.html)A month-of-year, such as 'July'.[MonthDay](MonthDay.html)A month-day in the ISO-8601 calendar system, such as `--12-03`.[OffsetDateTime](OffsetDateTime.html)A date-time with an offset from UTC/Greenwich in the ISO-8601 calendar system, such as `2007-12-03T10:15:30+01:00`.[OffsetTime](OffsetTime.html)A time with an offset from UTC/Greenwich in the ISO-8601 calendar system, such as `10:15:30+01:00`.[Period](Period.html)A date-based amount of time in the ISO-8601 calendar system, such as '2 years, 3 months and 4 days'.[Year](Year.html)A year in the ISO-8601 calendar system, such as `2007`.[YearMonth](YearMonth.html)A year-month in the ISO-8601 calendar system, such as `2007-12`.[ZonedDateTime](ZonedDateTime.html)A date-time with a time-zone in the ISO-8601 calendar system, such as `2007-12-03T10:15:30+01:00 Europe/Paris`.[ZoneId](ZoneId.html)A time-zone ID, such as `Europe/Paris`.[ZoneOffset](ZoneOffset.html)A time-zone offset from Greenwich/UTC, such as `+02:00`.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
