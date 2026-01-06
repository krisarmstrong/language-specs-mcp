# Messages[¶](#messages)
Version: 4.0.4

Source: https://pylint.readthedocs.io/en/stable/user_guide/messages/index.html


## Messages categories[¶](#messages-categories)

Pylint can emit various messages. These are categorized according to categories corresponding to bit-encoded exit codes:

- 

[Fatal](messages_overview.html#fatal-category) (1)

- 

[Error](messages_overview.html#error-category) (2)

- 

[Warning](messages_overview.html#warning-category) (4)

- 

[Convention](messages_overview.html#convention-category) (8)

- 

[Refactor](messages_overview.html#refactor-category) (16)

- 

[Information](messages_overview.html#information-category) (NA)

An overview of these messages can be found in [Messages overview](messages_overview.html#messages-overview)

## Disabling messages[¶](#disabling-messages)

`pylint` has an advanced message control for its checks, offering the ability to enable / disable a message either from the command line or from the configuration file, as well as from the code itself.

For more detail see [Messages control](message_control.html#message-control)
