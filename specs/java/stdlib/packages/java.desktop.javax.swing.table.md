Module[java.desktop](../../../module-summary.html)

# Package javax.swing.table

package javax.swing.tableProvides classes and interfaces for dealing with `javax.swing.JTable`. `JTable` is Swing's grid or tabular view for constructing user interfaces for tabular data structures inside an application. Use this package if you want control over how tables are constructed, updated, and rendered, as well as how data associated with the tables are viewed and managed. 

Note: Most of the Swing API is not thread safe. For details, see [Concurrency in Swing](https://docs.oracle.com/javase/tutorial/uiswing/concurrency/index.html), a section in [The Java Tutorial](https://docs.oracle.com/javase/tutorial/). 

## Related Documentation

 For overviews, tutorials, examples, guides, and tool documentation, please see: 

- [How to Use Tables](https://docs.oracle.com/javase/tutorial/uiswing/components/table.html), a section in The Java Tutorial

Since:1.2

- Related PackagesPackageDescription[javax.swing](../package-summary.html)Provides a set of "lightweight" (all-Java language) components that, to the maximum degree possible, work the same on all platforms.
- All Classes and InterfacesInterfacesClassesClassDescription[AbstractTableModel](AbstractTableModel.html)This abstract class provides default implementations for most of the methods in the `TableModel` interface.[DefaultTableCellRenderer](DefaultTableCellRenderer.html)The standard class for rendering (displaying) individual cells in a `JTable`.[DefaultTableCellRenderer.UIResource](DefaultTableCellRenderer.UIResource.html)A subclass of `DefaultTableCellRenderer` that implements `UIResource`.[DefaultTableColumnModel](DefaultTableColumnModel.html)The standard column-handler for a `JTable`.[DefaultTableModel](DefaultTableModel.html)This is an implementation of `TableModel` that uses a `Vector` of `Vectors` to store the cell value objects.[JTableHeader](JTableHeader.html)This is the object which manages the header of the `JTable`.[TableCellEditor](TableCellEditor.html)This interface must be implemented to provide an editor of cell values for a `JTable`.[TableCellRenderer](TableCellRenderer.html)This interface defines the method required by any object that would like to be a renderer for cells in a `JTable`.[TableColumn](TableColumn.html)A `TableColumn` represents all the attributes of a column in a `JTable`, such as width, resizability, minimum and maximum width.[TableColumnModel](TableColumnModel.html)Defines the requirements for a table column model object suitable for use with `JTable`.[TableModel](TableModel.html)The `TableModel` interface specifies the methods the `JTable` will use to interrogate a tabular data model.[TableRowSorter](TableRowSorter.html)<M extends [TableModel](TableModel.html)>An implementation of `RowSorter` that provides sorting and filtering using a `TableModel`.[TableStringConverter](TableStringConverter.html)TableStringConverter is used to convert objects from the model into strings.
