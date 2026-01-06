Module[java.management](../../../module-summary.html)

# Package javax.management.timer

package javax.management.timer

Provides the definition of the Timer MBean. A Timer MBean maintains a list of scheduled notifications and, because it is a [NotificationBroadcaster](../NotificationBroadcaster.html), a list of listeners for those notifications. Whenever the time for one of the scheduled notifications is reached, each listener receives the notification. Notifications can be repeated at a fixed interval, and the number of repetitions can be bounded.

A listener for a Timer MBean can itself be an MBean, using the method [MBeanServer.addNotificationListener(ObjectName, ObjectName, NotificationFilter, Object)](../MBeanServer.html#addNotificationListener(javax.management.ObjectName,javax.management.ObjectName,javax.management.NotificationFilter,java.lang.Object)). In this way, a management application can create an MBean representing a task, then schedule that task using a Timer MBean.

Since:1.5

- Related PackagesPackageDescription[javax.management](../package-summary.html)Provides the core classes for the Java Management Extensions.
- All Classes and InterfacesInterfacesClassesClassDescription[Timer](Timer.html)Provides the implementation of the timer MBean.[TimerMBean](TimerMBean.html)Exposes the management interface of the timer MBean.[TimerNotification](TimerNotification.html)This class provides definitions of the notifications sent by timer MBeans.
