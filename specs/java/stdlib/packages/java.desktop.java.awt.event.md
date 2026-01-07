java.awt.event (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

- [Overview](../../../../index.html)
- [Module](../../../module-summary.html)
- Package
- Class
- [Use](package-use.html)
- [Tree](package-tree.html)
- [Preview](../../../../preview-list.html)
- [New](../../../../new-list.html)
- [Deprecated](../../../../deprecated-list.html)
- [Index](../../../../index-files/index-1.html)
- [Help](../../../../help-doc.html#package)

- 

Package:

  - [Description](#package-description)
  - [Related Packages](#related-package-summary)
  - [Classes and Interfaces](#class-summary)

- Package: 
- [Description](#package-description) | 
- [Related Packages](#related-package-summary) | 
- [Classes and Interfaces](#class-summary)

[SEARCH](../../../../search.html)Module[java.desktop](../../../module-summary.html)

# Package java.awt.event

package java.awt.eventProvides interfaces and classes for dealing with different types of events fired by AWT components. See the [java.awt.AWTEvent](../AWTEvent.html) class for details on the AWT event model. Events are fired by event sources. An event listener registers with an event source to receive notifications about the events of a particular type. This package defines events and event listeners, as well as event listener adapters, which are convenience classes to make easier the process of writing event listeners.Since:1.1

- Related PackagesPackageDescription[java.awt](../package-summary.html)Contains all of the classes for creating user interfaces and for painting graphics and images.
- All Classes and InterfacesInterfacesClassesEnum ClassesClassDescription[ActionEvent](ActionEvent.html)A semantic event which indicates that a component-defined action occurred.[ActionListener](ActionListener.html)The listener interface for receiving action events.[AdjustmentEvent](AdjustmentEvent.html)The adjustment event emitted by Adjustable objects like [Scrollbar](../Scrollbar.html) and [ScrollPane](../ScrollPane.html).[AdjustmentListener](AdjustmentListener.html)The listener interface for receiving adjustment events.[AWTEventListener](AWTEventListener.html)The listener interface for receiving notification of events dispatched to objects that are instances of Component or MenuComponent or their subclasses.[AWTEventListenerProxy](AWTEventListenerProxy.html)A class which extends the `EventListenerProxy` specifically for adding an `AWTEventListener` for a specific event mask.[ComponentAdapter](ComponentAdapter.html)An abstract adapter class for receiving component events.[ComponentEvent](ComponentEvent.html)A low-level event which indicates that a component moved, changed size, or changed visibility (also, the root class for the other component-level events).[ComponentListener](ComponentListener.html)The listener interface for receiving component events.[ContainerAdapter](ContainerAdapter.html)An abstract adapter class for receiving container events.[ContainerEvent](ContainerEvent.html)A low-level event which indicates that a container's contents changed because a component was added or removed.[ContainerListener](ContainerListener.html)The listener interface for receiving container events.[FocusAdapter](FocusAdapter.html)An abstract adapter class for receiving keyboard focus events.[FocusEvent](FocusEvent.html)A low-level event which indicates that a Component has gained or lost the input focus.[FocusEvent.Cause](FocusEvent.Cause.html)This enum represents the cause of a `FocusEvent`- the reason why it occurred.[FocusListener](FocusListener.html)The listener interface for receiving keyboard focus events on a component.[HierarchyBoundsAdapter](HierarchyBoundsAdapter.html)An abstract adapter class for receiving ancestor moved and resized events.[HierarchyBoundsListener](HierarchyBoundsListener.html)The listener interface for receiving ancestor moved and resized events.[HierarchyEvent](HierarchyEvent.html)An event which indicates a change to the `Component` hierarchy to which `Component` belongs.[HierarchyListener](HierarchyListener.html)The listener interface for receiving hierarchy changed events.[InputEvent](InputEvent.html)The root event class for all component-level input events.[InputMethodEvent](InputMethodEvent.html)Input method events contain information about text that is being composed using an input method.[InputMethodListener](InputMethodListener.html)The listener interface for receiving input method events.[InvocationEvent](InvocationEvent.html)An event which executes the `run()` method on a `Runnable` when dispatched by the AWT event dispatcher thread.[ItemEvent](ItemEvent.html)A semantic event which indicates that an item was selected or deselected.[ItemListener](ItemListener.html)The listener interface for receiving item events.[KeyAdapter](KeyAdapter.html)An abstract adapter class for receiving keyboard events.[KeyEvent](KeyEvent.html)An event which indicates that a keystroke occurred in a component.[KeyListener](KeyListener.html)The listener interface for receiving keyboard events (keystrokes).[MouseAdapter](MouseAdapter.html)An abstract adapter class for receiving mouse events.[MouseEvent](MouseEvent.html)An event which indicates that a mouse action occurred in a component.[MouseListener](MouseListener.html)The listener interface for receiving "interesting" mouse events (press, release, click, enter, and exit) on a component.[MouseMotionAdapter](MouseMotionAdapter.html)An abstract adapter class for receiving mouse motion events.[MouseMotionListener](MouseMotionListener.html)The listener interface for receiving mouse motion events on a component.[MouseWheelEvent](MouseWheelEvent.html)An event which indicates that the mouse wheel was rotated in a component.[MouseWheelListener](MouseWheelListener.html)The listener interface for receiving mouse wheel events on a component.[PaintEvent](PaintEvent.html)The component-level paint event.[TextEvent](TextEvent.html)A semantic event which indicates that an object's text changed.[TextListener](TextListener.html)The listener interface for receiving text events.[WindowAdapter](WindowAdapter.html)An abstract adapter class for receiving window events.[WindowEvent](WindowEvent.html)A low-level event that indicates that a window has changed its status.[WindowFocusListener](WindowFocusListener.html)The listener interface for receiving `WindowEvents`, including `WINDOW_GAINED_FOCUS` and `WINDOW_LOST_FOCUS` events.[WindowListener](WindowListener.html)The listener interface for receiving window events.[WindowStateListener](WindowStateListener.html)The listener interface for receiving window state events.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
