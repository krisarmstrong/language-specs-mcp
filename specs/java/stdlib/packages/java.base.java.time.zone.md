Module[java.base](../../../module-summary.html)

# Package java.time.zone

package java.time.zone

 Support for time-zones and their rules. 

 Daylight Saving Time and Time-Zones are concepts used by Governments to alter local time. This package provides support for time-zones, their rules and the resulting gaps and overlaps in the local time-line typically caused by Daylight Saving Time. 

## Package specification

 Unless otherwise noted, passing a null argument to a constructor or method in any class or interface in this package will cause a [NullPointerException](../../lang/NullPointerException.html) to be thrown. The Javadoc "@param" definition is used to summarise the null-behavior. The "@throws [NullPointerException](../../lang/NullPointerException.html)" is not explicitly documented in each method. 

 All calculations should check for numeric overflow and throw either an [ArithmeticException](../../lang/ArithmeticException.html) or a [DateTimeException](../DateTimeException.html). 

Since:1.8

- Related PackagesPackageDescription[java.time](../package-summary.html) The main API for dates, times, instants, and durations.[java.time.chrono](../chrono/package-summary.html) Generic API for calendar systems other than the default ISO.[java.time.format](../format/package-summary.html) Provides classes to print and parse dates and times.[java.time.temporal](../temporal/package-summary.html) Access to date and time using fields and units, and date time adjusters.
- All Classes and InterfacesClassesEnum ClassesException ClassesClassDescription[ZoneOffsetTransition](ZoneOffsetTransition.html)A transition between two offsets caused by a discontinuity in the local time-line.[ZoneOffsetTransitionRule](ZoneOffsetTransitionRule.html)A rule expressing how to create a transition.[ZoneOffsetTransitionRule.TimeDefinition](ZoneOffsetTransitionRule.TimeDefinition.html)A definition of the way a local time can be converted to the actual transition date-time.[ZoneRules](ZoneRules.html)The rules defining how the zone offset varies for a single time-zone.[ZoneRulesException](ZoneRulesException.html)Thrown to indicate a problem with time-zone configuration.[ZoneRulesProvider](ZoneRulesProvider.html)Provider of time-zone rules to the system.
