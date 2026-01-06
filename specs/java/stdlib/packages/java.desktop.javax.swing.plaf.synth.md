Module[java.desktop](../../../../module-summary.html)

# Package javax.swing.plaf.synth

package javax.swing.plaf.synthSynth is a skinnable look and feel in which all painting is delegated. Synth does not provide a default look. In order to use Synth you need to specify a [file](doc-files/synthFileFormat.html), or provide a [SynthStyleFactory](SynthStyleFactory.html). Both configuration options require an understanding of the synth architecture, which is described below, as well as an understanding of Swing's architecture. 

 Unless otherwise specified null is not a legal value to any of the methods defined in the synth package and if passed in will result in a `NullPointerException`. 

## Synth

 Each [ComponentUI](../ComponentUI.html) implementation in Synth associates itself with one [SynthStyle](SynthStyle.html) per [Region](Region.html), most `Components` only have one `Region` and therefore only one `SynthStyle`. `SynthStyle` is used to access all style related properties: fonts, colors and other `Component` properties. In addition `SynthStyle`s are used to obtain [SynthPainter](SynthPainter.html)s for painting the background, border, focus and other portions of a `Component`. The `ComponentUI`s obtain `SynthStyle`s from a [SynthStyleFactory](SynthStyleFactory.html). A `SynthStyleFactory` can be provided directly by way of [SynthLookAndFeel.setStyleFactory(javax.swing.plaf.synth.SynthStyleFactory)](SynthLookAndFeel.html#setStyleFactory(javax.swing.plaf.synth.SynthStyleFactory)), or indirectly by way of [SynthLookAndFeel.load(java.io.InputStream, java.lang.Class<?>)](SynthLookAndFeel.html#load(java.io.InputStream,java.lang.Class)). The following example uses the `SynthLookAndFeel.load()` method to configure a `SynthLookAndFeel` and sets it as the current look and feel: 

```

     SynthLookAndFeel laf = new SynthLookAndFeel();
     laf.load(MyClass.class.getResourceAsStream("laf.xml"), MyClass.class);
     UIManager.setLookAndFeel(laf);
 
```

 Many `JComponent`s are broken down into smaller pieces and identified by the type safe enumeration in [Region](Region.html). For example, a `JTabbedPane` consists of a `Region` for the `JTabbedPane`([Region.TABBED_PANE](Region.html#TABBED_PANE)), the content area ([Region.TABBED_PANE_CONTENT](Region.html#TABBED_PANE_CONTENT)), the area behind the tabs ([Region.TABBED_PANE_TAB_AREA](Region.html#TABBED_PANE_TAB_AREA)), and the tabs ([Region.TABBED_PANE_TAB](Region.html#TABBED_PANE_TAB)). Each `Region` of each `JComponent` will have a `SynthStyle`. This allows you to customize individual pieces of each region of each `JComponent`. 

 Many of the Synth methods take a [SynthContext](SynthContext.html). This is used to provide information about the current `Component` and includes: the [SynthStyle](SynthStyle.html) associated with the current [Region](Region.html), the state of the `Component` as a bitmask (refer to [SynthConstants](SynthConstants.html) for the valid states), and a [Region](Region.html) identifying the portion of the `Component` being painted. 

 All text rendering by non-`JTextComponent`s is delegated to a [SynthGraphicsUtils](SynthGraphicsUtils.html), which is obtained using the [SynthStyle](SynthStyle.html) method [SynthStyle.getGraphicsUtils(javax.swing.plaf.synth.SynthContext)](SynthStyle.html#getGraphicsUtils(javax.swing.plaf.synth.SynthContext)). You can customize text rendering by supplying your own [SynthGraphicsUtils](SynthGraphicsUtils.html). 

## Notes on specific components

### JTree

 Synth provides a region for the cells of a tree: `Region.TREE_CELL`. To specify the colors of the renderer you'll want to provide a style for the `TREE_CELL` region. The following illustrates this: 

```

   <style id="treeCellStyle">
     <opaque value="TRUE"/>
     <state>
       <color value="WHITE" type="TEXT_FOREGROUND"/>
       <color value="RED" type="TEXT_BACKGROUND"/>
     </state>
     <state value="SELECTED">
       <color value="RED" type="TEXT_FOREGROUND"/>
       <color value="WHITE" type="BACKGROUND"/>
     </state>
   </style>
   <bind style="treeCellStyle" type="region" key="TreeCell"/>
 
```

 This specifies a color combination of red on white, when selected, and white on red when not selected. To see the background you need to specify that labels are not opaque. The following XML fragment does that: 

```

   <style id="labelStyle">
     <opaque value="FALSE"/>
   </style>
   <bind style="labelStyle" type="region" key="Label"/>
 
```

### JList and JTable

 The colors that the renderers for JList and JTable use are specified by way of the list and table Regions. The following XML fragment illustrates how to specify red on white, when selected, and white on red when not selected: 

```

   <style id="style">
     <opaque value="TRUE"/>
     <state>
       <color value="WHITE" type="TEXT_FOREGROUND"/>
       <color value="RED" type="TEXT_BACKGROUND"/>
       <color value="RED" type="BACKGROUND"/>
     </state>
     <state value="SELECTED">
       <color value="RED" type="TEXT_FOREGROUND"/>
       <color value="WHITE" type="TEXT_BACKGROUND"/>
     </state>
   </style>
   <bind style="style" type="region" key="Table"/>
   <bind style="style" type="region" key="List"/>
 
```

- Related PackagesPackageDescription[javax.swing.plaf](../package-summary.html)Provides one interface and many abstract classes that Swing uses to provide its pluggable look-and-feel capabilities.[javax.swing.plaf.basic](../basic/package-summary.html)Provides user interface objects built according to the Basic look and feel.[javax.swing.plaf.metal](../metal/package-summary.html)Provides user interface objects built according to the Java look and feel (once codenamed Metal), which is the default look and feel.[javax.swing.plaf.multi](../multi/package-summary.html)Provides user interface objects that combine two or more look and feels.[javax.swing.plaf.nimbus](../nimbus/package-summary.html)Provides user interface objects built according to the cross-platform Nimbus look and feel.
- All Classes and InterfacesInterfacesClassesClassDescription[ColorType](ColorType.html)A typesafe enumeration of colors that can be fetched from a style.[Region](Region.html)A distinct rendering area of a Swing component.[SynthButtonUI](SynthButtonUI.html)Provides the Synth L&F UI delegate for [JButton](../../JButton.html).[SynthCheckBoxMenuItemUI](SynthCheckBoxMenuItemUI.html)Provides the Synth L&F UI delegate for [JCheckBoxMenuItem](../../JCheckBoxMenuItem.html).[SynthCheckBoxUI](SynthCheckBoxUI.html)Provides the Synth L&F UI delegate for [JCheckBox](../../JCheckBox.html).[SynthColorChooserUI](SynthColorChooserUI.html)Provides the Synth L&F UI delegate for [JColorChooser](../../JColorChooser.html).[SynthComboBoxUI](SynthComboBoxUI.html)Provides the Synth L&F UI delegate for [JComboBox](../../JComboBox.html).[SynthConstants](SynthConstants.html)Constants used by Synth.[SynthContext](SynthContext.html)An immutable transient object containing contextual information about a `Region`.[SynthDesktopIconUI](SynthDesktopIconUI.html)Provides the Synth L&F UI delegate for a minimized internal frame on a desktop.[SynthDesktopPaneUI](SynthDesktopPaneUI.html)Provides the Synth L&F UI delegate for [JDesktopPane](../../JDesktopPane.html).[SynthEditorPaneUI](SynthEditorPaneUI.html)Provides the Synth L&F UI delegate for [JEditorPane](../../JEditorPane.html).[SynthFormattedTextFieldUI](SynthFormattedTextFieldUI.html)Provides the Synth L&F UI delegate for [JFormattedTextField](../../JFormattedTextField.html).[SynthGraphicsUtils](SynthGraphicsUtils.html)Wrapper for primitive graphics calls.[SynthIcon](SynthIcon.html)An icon that is passed a `SynthContext`.[SynthInternalFrameUI](SynthInternalFrameUI.html)Provides the Synth L&F UI delegate for [JInternalFrame](../../JInternalFrame.html).[SynthLabelUI](SynthLabelUI.html)Provides the Synth L&F UI delegate for [JLabel](../../JLabel.html).[SynthListUI](SynthListUI.html)Provides the Synth L&F UI delegate for [JList](../../JList.html).[SynthLookAndFeel](SynthLookAndFeel.html)SynthLookAndFeel provides the basis for creating a customized look and feel.[SynthMenuBarUI](SynthMenuBarUI.html)Provides the Synth L&F UI delegate for [JMenuBar](../../JMenuBar.html).[SynthMenuItemUI](SynthMenuItemUI.html)Provides the Synth L&F UI delegate for [JMenuItem](../../JMenuItem.html).[SynthMenuUI](SynthMenuUI.html)Provides the Synth L&F UI delegate for [JMenu](../../JMenu.html).[SynthOptionPaneUI](SynthOptionPaneUI.html)Provides the Synth L&F UI delegate for [JOptionPane](../../JOptionPane.html).[SynthPainter](SynthPainter.html)`SynthPainter` is used for painting portions of `JComponent`s.[SynthPanelUI](SynthPanelUI.html)Provides the Synth L&F UI delegate for [JPanel](../../JPanel.html).[SynthPasswordFieldUI](SynthPasswordFieldUI.html)Provides the Synth L&F UI delegate for [JPasswordField](../../JPasswordField.html).[SynthPopupMenuUI](SynthPopupMenuUI.html)Provides the Synth L&F UI delegate for [JPopupMenu](../../JPopupMenu.html).[SynthProgressBarUI](SynthProgressBarUI.html)Provides the Synth L&F UI delegate for [JProgressBar](../../JProgressBar.html).[SynthRadioButtonMenuItemUI](SynthRadioButtonMenuItemUI.html)Provides the Synth L&F UI delegate for [JRadioButtonMenuItem](../../JRadioButtonMenuItem.html).[SynthRadioButtonUI](SynthRadioButtonUI.html)Provides the Synth L&F UI delegate for [JRadioButton](../../JRadioButton.html).[SynthRootPaneUI](SynthRootPaneUI.html)Provides the Synth L&F UI delegate for [JRootPane](../../JRootPane.html).[SynthScrollBarUI](SynthScrollBarUI.html)Provides the Synth L&F UI delegate for [JScrollBar](../../JScrollBar.html).[SynthScrollPaneUI](SynthScrollPaneUI.html)Provides the Synth L&F UI delegate for [JScrollPane](../../JScrollPane.html).[SynthSeparatorUI](SynthSeparatorUI.html)Provides the Synth L&F UI delegate for [JSeparator](../../JSeparator.html).[SynthSliderUI](SynthSliderUI.html)Provides the Synth L&F UI delegate for [JSlider](../../JSlider.html).[SynthSpinnerUI](SynthSpinnerUI.html)Provides the Synth L&F UI delegate for [JSpinner](../../JSpinner.html).[SynthSplitPaneUI](SynthSplitPaneUI.html)Provides the Synth L&F UI delegate for [JSplitPane](../../JSplitPane.html).[SynthStyle](SynthStyle.html)`SynthStyle` is a set of style properties.[SynthStyleFactory](SynthStyleFactory.html)Factory used for obtaining `SynthStyle`s.[SynthTabbedPaneUI](SynthTabbedPaneUI.html)Provides the Synth L&F UI delegate for [JTabbedPane](../../JTabbedPane.html).[SynthTableHeaderUI](SynthTableHeaderUI.html)Provides the Synth L&F UI delegate for [JTableHeader](../../table/JTableHeader.html).[SynthTableUI](SynthTableUI.html)Provides the Synth L&F UI delegate for [JTable](../../JTable.html).[SynthTextAreaUI](SynthTextAreaUI.html)Provides the look and feel for a plain text editor in the Synth look and feel.[SynthTextFieldUI](SynthTextFieldUI.html)Provides the Synth L&F UI delegate for [JTextField](../../JTextField.html).[SynthTextPaneUI](SynthTextPaneUI.html)Provides the look and feel for a styled text editor in the Synth look and feel.[SynthToggleButtonUI](SynthToggleButtonUI.html)Provides the Synth L&F UI delegate for [JToggleButton](../../JToggleButton.html).[SynthToolBarUI](SynthToolBarUI.html)Provides the Synth L&F UI delegate for [JToolBar](../../JToolBar.html).[SynthToolTipUI](SynthToolTipUI.html)Provides the Synth L&F UI delegate for [JToolTip](../../JToolTip.html).[SynthTreeUI](SynthTreeUI.html)Provides the Synth L&F UI delegate for [JTree](../../JTree.html).[SynthUI](SynthUI.html)SynthUI is used to fetch the SynthContext for a particular Component.[SynthViewportUI](SynthViewportUI.html)Provides the Synth L&F UI delegate for [JViewport](../../JViewport.html).
