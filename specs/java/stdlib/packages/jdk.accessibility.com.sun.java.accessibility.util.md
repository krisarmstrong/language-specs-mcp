Module[jdk.accessibility](../../../../../module-summary.html)

# Package com.sun.java.accessibility.util

package com.sun.java.accessibility.utilProvides a collection of interfaces and classes that compose the Java Accessibility Utilities. The classes are used by Assistive Technologies, such as the screen readers which are used by those who are blind, and help provide access to GUI toolkits that implement the Java Accessibility API. An overview of the important classes follows. 

The class `AccessibilityEventMonitor` implements a PropertyChange listener on every UI object that implements interface `Accessible` in the Java Virtual Machine. 

 The class `AWTEventMonitor` implements a suite of listeners that are conditionally installed on every AWT component instance in the Java Virtual Machine. 

The class `EventQueueMonitor` provides key core functionality for Assistive Technologies (and other system-level technologies that need some of the same things that Assistive Technology needs). 

The class `GUIInitializedMulticaster` is used to maintain a list of `GUIInitializedListener` classes which are used by the `EventQueueMonitor` class to notify an interested party when the GUI subsystem has been initialized. Note that this class is intended to be used primarily for internal support in the `EventQueueMonitor` class, and is not intended to be used by classes outside the Java Accessibility Utility package. 

The class `SwingEventMonitor` extends `AWTEventMonitor` by adding a suite of listeners conditionally installed on every Swing component instance in the Java Virtual Machine. 

The class `TopLevelWindowMulticaster` is used to maintain a list of `TopLevelWindowListener` classes which are used by the `EventQueueMonitor` class to notify an interested party when a top level window is created or destroyed in the Java Virtual Machine Note that this class is intended to be used primarily for internal support in the `EventQueueMonitor` class, and is not intended to be used by classes outside the Java Accessibility Utility package. 

The class `Translator` provides a translation to interface `Accessible` for objects that do not implement interface `Accessible`.

Since:JDK1.7

- All Classes and InterfacesInterfacesClassesClassDescription[AccessibilityEventMonitor](AccessibilityEventMonitor.html)`AccessibilityEventMonitor` implements a PropertyChange listener on every UI object that implements interface `Accessible` in the Java Virtual Machine.[AccessibilityListenerList](AccessibilityListenerList.html)The `AccessibilityListenerList` is a copy of the Swing [EventListerList](../../../../../../java.desktop/javax/swing/event/EventListenerList.html) class.[AWTEventMonitor](AWTEventMonitor.html)The `AWTEventMonitor` implements a suite of listeners that are conditionally installed on every AWT component instance in the Java Virtual Machine.[EventID](EventID.html)EventID contains integer constants that map to event support in AWT and Swing.[EventQueueMonitor](EventQueueMonitor.html)The `EventQueueMonitor` class provides key core functionality for Assistive Technologies (and other system-level technologies that need some of the same things that Assistive Technology needs).[GUIInitializedListener](GUIInitializedListener.html)The `GUIInitializedListener` interface is used by the [EventQueueMonitor](EventQueueMonitor.html) class to notify an interested party when the GUI subsystem has been initialized.[SwingEventMonitor](SwingEventMonitor.html)`SwingEventMonitor` extends [AWTEventMonitor](AWTEventMonitor.html) by adding a suite of listeners conditionally installed on every Swing component instance in the Java Virtual Machine.[TopLevelWindowListener](TopLevelWindowListener.html)The `TopLevelWindowListener` interface is used by the [EventQueueMonitor](EventQueueMonitor.html) class to notify an interested party when a top level window is created or destroyed in the Java Virtual Machine.[Translator](Translator.html)The `Translator` class provides a translation to interface [Accessible](../../../../../../java.desktop/javax/accessibility/Accessible.html) for objects that do not implement interface `Accessible`.
