Module[java.base](../../../module-summary.html)

# Package java.time.temporal

package java.time.temporal

 Access to date and time using fields and units, and date time adjusters. 

 This package expands on the base package to provide additional functionality for more powerful use cases. Support is included for: 

- Units of date-time, such as years, months, days and hours
- Fields of date-time, such as month-of-year, day-of-week or hour-of-day
- Date-time adjustment functions
- Different definitions of weeks

## Fields and Units

 Dates and times are expressed in terms of fields and units. A unit is used to measure an amount of time, such as years, days or minutes. All units implement [TemporalUnit](TemporalUnit.html). The set of well known units is defined in [ChronoUnit](ChronoUnit.html), such as `DAYS`. The unit interface is designed to allow application defined units. 

 A field is used to express part of a larger date-time, such as year, month-of-year or second-of-minute. All fields implement [TemporalField](TemporalField.html). The set of well known fields are defined in [ChronoField](ChronoField.html), such as `HOUR_OF_DAY`. Additional fields are defined by [JulianFields](JulianFields.html), [WeekFields](WeekFields.html) and [IsoFields](IsoFields.html). The field interface is designed to allow application defined fields. 

 This package provides tools that allow the units and fields of date and time to be accessed in a general way most suited for frameworks. [Temporal](Temporal.html) provides the abstraction for date time types that support fields. Its methods support getting the value of a field, creating a new date time with the value of a field modified, and querying for additional information, typically used to extract the offset or time-zone. 

 One use of fields in application code is to retrieve fields for which there is no convenience method. For example, getting the day-of-month is common enough that there is a method on `LocalDate` called `getDayOfMonth()`. However for more unusual fields it is necessary to use the field. For example, `date.get(ChronoField.ALIGNED_WEEK_OF_MONTH)`. The fields also provide access to the range of valid values. 

## Adjustment and Query

 A key part of the date-time problem space is adjusting a date to a new, related value, such as the "last day of the month", or "next Wednesday". These are modeled as functions that adjust a base date-time. The functions implement [TemporalAdjuster](TemporalAdjuster.html) and operate on `Temporal`. A set of common functions are provided in [TemporalAdjusters](TemporalAdjusters.html). For example, to find the first occurrence of a day-of-week after a given date, use [TemporalAdjusters.next(DayOfWeek)](TemporalAdjusters.html#next(java.time.DayOfWeek)), such as `date.with(next(MONDAY))`. Applications can also define adjusters by implementing [TemporalAdjuster](TemporalAdjuster.html). 

 The [TemporalAmount](TemporalAmount.html) interface models amounts of relative time. 

 In addition to adjusting a date-time, an interface is provided to enable querying via [TemporalQuery](TemporalQuery.html). The most common implementations of the query interface are method references. The `from(TemporalAccessor)` methods on major classes can all be used, such as `LocalDate::from` or `Month::from`. Further implementations are provided in [TemporalQueries](TemporalQueries.html) as static methods. Applications can also define queries by implementing [TemporalQuery](TemporalQuery.html). 

## Weeks

 Different locales have different definitions of the week. For example, in Europe the week typically starts on a Monday, while in the US it starts on a Sunday. The [WeekFields](WeekFields.html) class models this distinction. 

 The ISO calendar system defines an additional week-based division of years. This defines a year based on whole Monday to Monday weeks. This is modeled in [IsoFields](IsoFields.html). 

## Package specification

 Unless otherwise noted, passing a null argument to a constructor or method in any class or interface in this package will cause a [NullPointerException](../../lang/NullPointerException.html) to be thrown. The Javadoc "@param" definition is used to summarise the null-behavior. The "@throws [NullPointerException](../../lang/NullPointerException.html)" is not explicitly documented in each method. 

 All calculations should check for numeric overflow and throw either an [ArithmeticException](../../lang/ArithmeticException.html) or a [DateTimeException](../DateTimeException.html). 

Since:1.8

- Related PackagesPackageDescription[java.time](../package-summary.html) The main API for dates, times, instants, and durations.[java.time.chrono](../chrono/package-summary.html) Generic API for calendar systems other than the default ISO.[java.time.format](../format/package-summary.html) Provides classes to print and parse dates and times.[java.time.zone](../zone/package-summary.html) Support for time-zones and their rules.
- All Classes and InterfacesInterfacesClassesEnum ClassesException ClassesClassDescription[ChronoField](ChronoField.html)A standard set of fields.[ChronoUnit](ChronoUnit.html)A standard set of date periods units.[IsoFields](IsoFields.html)Fields and units specific to the ISO-8601 calendar system, including quarter-of-year and week-based-year.[JulianFields](JulianFields.html)A set of date fields that provide access to Julian Days.[Temporal](Temporal.html)Framework-level interface defining read-write access to a temporal object, such as a date, time, offset or some combination of these.[TemporalAccessor](TemporalAccessor.html)Framework-level interface defining read-only access to a temporal object, such as a date, time, offset or some combination of these.[TemporalAdjuster](TemporalAdjuster.html)Strategy for adjusting a temporal object.[TemporalAdjusters](TemporalAdjusters.html)Common and useful TemporalAdjusters.[TemporalAmount](TemporalAmount.html)Framework-level interface defining an amount of time, such as "6 hours", "8 days" or "2 years and 3 months".[TemporalField](TemporalField.html)A field of date-time, such as month-of-year or minute-of-hour.[TemporalQueries](TemporalQueries.html)Common implementations of `TemporalQuery`.[TemporalQuery](TemporalQuery.html)<R>Strategy for querying a temporal object.[TemporalUnit](TemporalUnit.html)A unit of date-time, such as Days or Hours.[UnsupportedTemporalTypeException](UnsupportedTemporalTypeException.html)UnsupportedTemporalTypeException indicates that a ChronoField or ChronoUnit is not supported for a Temporal class.[ValueRange](ValueRange.html)The range of valid values for a date-time field.[WeekFields](WeekFields.html)Localized definitions of the day-of-week, week-of-month and week-of-year fields.
