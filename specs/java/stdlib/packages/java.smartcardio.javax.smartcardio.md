Module[java.smartcardio](../../module-summary.html)

# Package javax.smartcardio

package javax.smartcardioJava™ Smart Card I/O API. This specification describes the Java Smart Card I/O API defined by [JSR 268](http://jcp.org/en/jsr/detail?id=268). It defines a Java API for communication with Smart Cards using ISO/IEC 7816-4 APDUs. It thereby allows Java applications to interact with applications running on the Smart Card, to store and retrieve data on the card, etc. 

 The API is defined by classes in the package `javax.smartcardio`. They can be classified as follows: Classes describing the corresponding Smart Card structures [ATR](ATR.html), [CommandAPDU](CommandAPDU.html), [ResponseAPDU](ResponseAPDU.html)Factory to obtain implementations [TerminalFactory](TerminalFactory.html)Main classes for card and terminal functions [CardTerminals](CardTerminals.html), [CardTerminal](CardTerminal.html), [Card](Card.html), [CardChannel](CardChannel.html)Supporting permission and exception classes [CardPermission](CardPermission.html), [CardException](CardException.html), [CardNotPresentException](CardNotPresentException.html)Service provider interface, not accessed directly by applications [TerminalFactorySpi](TerminalFactorySpi.html)

## API Example

 A simple example of using the API is: 

```

      // show the list of available terminals
      TerminalFactory factory = TerminalFactory.getDefault();
      List<CardTerminal> terminals = factory.terminals().list();
      System.out.println("Terminals: " + terminals);
      // get the first terminal
      CardTerminal terminal = terminals.get(0);
      // establish a connection with the card
      Card card = terminal.connect("T=0");
      System.out.println("card: " + card);
      CardChannel channel = card.getBasicChannel();
      ResponseAPDU r = channel.transmit(new CommandAPDU(c1));
      System.out.println("response: " + toString(r.getBytes()));
      // disconnect
      card.disconnect(false);
 
```

Since:1.6

- All Classes and InterfacesClassesEnum ClassesException ClassesClassDescription[ATR](ATR.html)A Smart Card's answer-to-reset bytes.[Card](Card.html)A Smart Card with which a connection has been established.[CardChannel](CardChannel.html)A logical channel connection to a Smart Card.[CardException](CardException.html)Exception for errors that occur during communication with the Smart Card stack or the card itself.[CardNotPresentException](CardNotPresentException.html)Exception thrown when an application tries to establish a connection with a terminal that has no card present.[CardPermission](CardPermission.html)A permission for Smart Card operations.[CardTerminal](CardTerminal.html)A Smart Card terminal, sometimes referred to as a Smart Card Reader.[CardTerminals](CardTerminals.html)The set of terminals supported by a TerminalFactory.[CardTerminals.State](CardTerminals.State.html)Enumeration of attributes of a CardTerminal.[CommandAPDU](CommandAPDU.html)A command APDU following the structure defined in ISO/IEC 7816-4.[ResponseAPDU](ResponseAPDU.html)A response APDU as defined in ISO/IEC 7816-4.[TerminalFactory](TerminalFactory.html)A factory for CardTerminal objects.[TerminalFactorySpi](TerminalFactorySpi.html)The TerminalFactorySpi class defines the service provider interface.
