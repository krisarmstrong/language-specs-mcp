Module[java.desktop](../../../../module-summary.html)

# Package javax.swing.plaf.nimbus

package javax.swing.plaf.nimbusProvides user interface objects built according to the cross-platform Nimbus look and feel. 

 Nimbus uses instances of the [Painter](../../Painter.html) interface to paint components. With each Swing component it associates a foreground and a background `Painter`, and there may be several painters for different component states. 

 Nimbus allows customizing many of its properties, including painters, by altering the [UIDefaults](../../UIDefaults.html) table. Here's an example: 

```

 UIManager.put("ProgressBar.tileWidth", myTileWidth);
 UIManager.put("ProgressBar[Enabled].backgroundPainter", myBgPainter);
 UIManager.put("ProgressBar[Enabled].foregroundPainter", myFgPainter);
 
```

 Per-component customization is also possible. When rendering a component, Nimbus checks its client property named "Nimbus.Overrides". The value of this property should be an instance of `UIDefaults`. Settings from that table override the UIManager settings, but for that particular component instance only. An optional client property, "Nimbus.Overrides.InheritDefaults" of type Boolean, specifies whether the overriding settings should be merged with default ones (`true`), or replace them (`false`). By default they are merged: 

```

 JProgressBar bar = new JProgressBar();
 UIDefaults overrides = new UIDefaults();
 overrides.put("ProgressBar.cycleTime", 330);
 ...
 bar.putClientProperty("Nimbus.Overrides", overrides);
 bar.putClientProperty("Nimbus.Overrides.InheritDefaults", false);
 
```

 Colors in Nimbus are derived from a core set of [primary colors](doc-files/properties.html#primaryColors). There are also [secondary colors](doc-files/properties.html#secondaryColors), which are derived from primary ones, but serve themselves as base colors for other derived colors. The derivation mechanism allows for runtime customization, i.e. if a primary or secondary color is changed, all colors that are derived from it are automatically updated. The method [NimbusLookAndFeel.getDerivedColor(java.lang.String, float, float, float, int, boolean)](NimbusLookAndFeel.html#getDerivedColor(java.lang.String,float,float,float,int,boolean)) may be used to create a derived color. 

 These classes are designed to be used while the corresponding `LookAndFeel` class has been installed (`UIManager.setLookAndFeel(new XXXLookAndFeel())`). Using them while a different `LookAndFeel` is installed may produce unexpected results, including exceptions. Additionally, changing the `LookAndFeel` maintained by the `UIManager` without updating the corresponding `ComponentUI` of any `JComponent`s may also produce unexpected results, such as the wrong colors showing up, and is generally not encouraged. 

Note: Most of the Swing API is not thread safe. For details, see [Concurrency in Swing](https://docs.oracle.com/javase/tutorial/uiswing/concurrency/index.html), a section in [The Java Tutorial](https://docs.oracle.com/javase/tutorial/).

Since:1.7

- Related PackagesPackageDescription[javax.swing.plaf](../package-summary.html)Provides one interface and many abstract classes that Swing uses to provide its pluggable look-and-feel capabilities.[javax.swing.plaf.basic](../basic/package-summary.html)Provides user interface objects built according to the Basic look and feel.[javax.swing.plaf.metal](../metal/package-summary.html)Provides user interface objects built according to the Java look and feel (once codenamed Metal), which is the default look and feel.[javax.swing.plaf.multi](../multi/package-summary.html)Provides user interface objects that combine two or more look and feels.[javax.swing.plaf.synth](../synth/package-summary.html)Synth is a skinnable look and feel in which all painting is delegated.
- All Classes and InterfacesClassesEnum ClassesClassDescription[AbstractRegionPainter](AbstractRegionPainter.html)Convenient base class for defining Painter instances for rendering a region or component in Nimbus.[AbstractRegionPainter.PaintContext](AbstractRegionPainter.PaintContext.html)A class encapsulating state useful when painting.[AbstractRegionPainter.PaintContext.CacheMode](AbstractRegionPainter.PaintContext.CacheMode.html)Cache mode.[NimbusLookAndFeel](NimbusLookAndFeel.html)The NimbusLookAndFeel class.[NimbusStyle](NimbusStyle.html)A SynthStyle implementation used by Nimbus.[State](State.html)<T extends [JComponent](../../JComponent.html)>Represents a built in, or custom, state in Nimbus.
