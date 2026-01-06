Table of contents Exit editor modeAsk LearnAsk LearnFocus modeTable of contents[Read in English](#)AddAdd to plan[Edit](https://github.com/MicrosoftDocs/windowsserverdocs/blob/main/WindowsServerDocs/administration/windows-commands/windows-commands.md)

#### Share via

[Facebook](#)[x.com](#)[LinkedIn](#)[Email](#)Print

Note

 Access to this page requires authorization. You can try [signing in](#) or changing directories. 

 Access to this page requires authorization. You can try changing directories. 

# Windows Commands

- Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows 11](https://learn.microsoft.com/windows/release-health/supported-versions-windows-client), ✅ [Windows 10](https://learn.microsoft.com/windows/release-health/supported-versions-windows-client), ✅ [Azure Local 2311.2 and later](https://learn.microsoft.com/azure/azure-local/release-information-23h2)

Feedback Summarize this article for me 

##  In this article 

All supported versions of Windows and Windows Server have a set of Win32 console commands built in. This set of documentation describes the Windows Commands you can use to automate tasks by using scripts or scripting tools.

## Command-line shells

Windows has two command-line shells: the Command shell and [PowerShell](/en-us/powershell/scripting/overview). Each shell is a software program that provides direct communication between you and the operating system or application, providing an environment to automate IT operations.

The Command shell was the first shell built into Windows to automate routine tasks, like user account management or nightly backups, with batch (.bat) files. With Windows Script Host, you could run more sophisticated scripts in the Command shell. For more information, see [cscript](cscript) or [wscript](wscript). You can perform operations more efficiently by using scripts than you can by using the user interface. Scripts accept all commands that are available at the command line.

PowerShell was designed to extend the capabilities of the Command shell to run PowerShell commands called cmdlets. Cmdlets are similar to Windows Commands but provide a more extensible scripting language. You can run both Windows Commands and PowerShell cmdlets in PowerShell, but the Command shell can only run Windows Commands and not PowerShell cmdlets.

For the most robust, up-to-date Windows automation, we recommend using PowerShell instead of Windows Commands or Windows Script Host for Windows automation.

A reference of exit and error codes for Windows Commands can be found in the [Debug system error codes](/en-us/windows/win32/debug/system-error-codes) articles that may be helpful to understanding errors produced. Windows Commands also include command redirection operators. To learn more of their use, see [Using command redirection operators](/en-us/previous-versions/windows/it-pro/windows-xp/bb490982(v=technet.10)).

Note

You can also download and install [PowerShell Core](/en-us/powershell/scripting/install/installing-powershell), the open source version of PowerShell.

## Command shell file and directory name automatic completion

You can configure the Command shell to automatically complete file and directory names on a computer or user session when a specified control character is pressed. By default this control character is configured to be the tab key for both file and directory names, although they can be different. To change this control character, run `regedit.exe` and navigate to either of the following registry keys and entries, depending on whether you wish to change the value for the current user only, or for all users of the computer.

Caution

Incorrectly editing the registry may severely damage your system. Before making the following changes to the registry, you should back up any valued data on the computer.

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Command Processor\CompletionChar
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Command Processor\PathCompletionChar
```

Set these values to that of the control character you wish to use. See [virtual key codes](/en-us/windows/win32/inputdev/virtual-key-codes) for a complete list. To disable a particular completion character in the registry, use the value for space (0x20) as it isn't a valid control character. The type of value for this registry entry is [REG_DWORD](/en-us/windows/win32/sysinfo/registry-value-types), and can also be specified by hexadecimal or decimal value.

You can also enable or disable file and directory name completion per instance of a Command shell by running `cmd.exe` with the parameter and switch `/F:ON` or `/F:OFF`. If name completion is enabled with the `/F:ON` parameter and switch, the two control characters used are `Ctrl-D` for directory name completion and `Ctrl-F` for file name completion. User-specified settings take precedence over computer settings, and command-line options take precedence over registry settings.

## Command-line reference A-Z

To find information about a specific command, in the following A-Z menu, select the letter that the command starts with, and then select the command name.

[A](#a) | [B](#b) | [C](#c) | [D](#d) | [E](#e) | [F](#f) | [G](#g) | [H](#h) | [I](#i) | [J](#j) | [K](#k) | [L](#l) | [M](#m) | [N](#n) | [O](#o) | [P](#p) | [Q](#q) | [R](#r) | [S](#s) | [T](#t) | [U](#u) | [V](#v) | [W](#w) | [X](#x) | Y | Z

### A

- [active](active)
- [add](add)
- [add alias](add-alias)
- [add volume](add-volume)
- [adprep](adprep)
- [append](append)
- [arp](arp)
- [assign](assign)
- [assoc](assoc)
- [at](at)
- [atmadm](atmadm)
- [attach-vdisk](attach-vdisk)
- [attrib](attrib)
- [attributes](attributes)

  - [attributes disk](attributes-disk)
  - [attributes volume](attributes-volume)

- [auditpol](auditpol)

  - [auditpol backup](auditpol-backup)
  - [auditpol clear](auditpol-clear)
  - [auditpol get](auditpol-get)
  - [auditpol list](auditpol-list)
  - [auditpol remove](auditpol-remove)
  - [auditpol resourcesacl](auditpol-resourcesacl)
  - [auditpol restore](auditpol-restore)
  - [auditpol set](auditpol-set)

- [autochk](autochk)
- [autoconv](autoconv)
- [autofmt](autofmt)
- [automount](automount)

### B

- [bcdboot](bcdboot)
- [bcdedit](bcdedit)
- [bdehdcfg](bdehdcfg)

  - [bdehdcfg driveinfo](bdehdcfg-driveinfo)
  - [bdehdcfg newdriveletter](bdehdcfg-newdriveletter)
  - [bdehdcfg quiet](bdehdcfg-quiet)
  - [bdehdcfg restart](bdehdcfg-restart)
  - [bdehdcfg size](bdehdcfg-size)
  - [bdehdcfg target](bdehdcfg-target)

- [begin backup](begin-backup)
- [begin restore](begin-restore)
- [bitsadmin](bitsadmin)

  - [bitsadmin addfile](bitsadmin-addfile)
  - [bitsadmin addfileset](bitsadmin-addfileset)
  - [bitsadmin addfilewithranges](bitsadmin-addfilewithranges)
  - [bitsadmin cache](bitsadmin-cache)

    - [bitsadmin cache and delete](bitsadmin-cache-and-delete)
    - [bitsadmin cache and deleteurl](bitsadmin-cache-and-deleteurl)
    - [bitsadmin cache and getexpirationtime](bitsadmin-cache-and-getexpirationtime)
    - [bitsadmin cache and getlimit](bitsadmin-cache-and-getlimit)
    - [bitsadmin cache and help](bitsadmin-cache-and-help)
    - [bitsadmin cache and info](bitsadmin-cache-and-info)
    - [bitsadmin cache and list](bitsadmin-cache-and-list)
    - [bitsadmin cache and setexpirationtime](bitsadmin-cache-and-setexpirationtime)
    - [bitsadmin cache and setlimit](bitsadmin-cache-and-setlimit)
    - [bitsadmin cache and clear](bitsadmin-cache-clear)

  - [bitsadmin cancel](bitsadmin-cancel)
  - [bitsadmin complete](bitsadmin-complete)
  - [bitsadmin create](bitsadmin-create)
  - [bitsadmin examples](bitsadmin-examples)
  - [bitsadmin getaclflags](bitsadmin-getaclflags)
  - [bitsadmin getbytestotal](bitsadmin-getbytestotal)
  - [bitsadmin getbytestransferred](bitsadmin-getbytestransferred)
  - [bitsadmin getclientcertificate](bitsadmin-getclientcertificate)
  - [bitsadmin getcompletiontime](bitsadmin-getcompletiontime)
  - [bitsadmin getcreationtime](bitsadmin-getcreationtime)
  - [bitsadmin getcustomheaders](bitsadmin-getcustomheaders)
  - [bitsadmin getdescription](bitsadmin-getdescription)
  - [bitsadmin getdisplayname](bitsadmin-getdisplayname)
  - [bitsadmin geterror](bitsadmin-geterror)
  - [bitsadmin geterrorcount](bitsadmin-geterrorcount)
  - [bitsadmin getfilestotal](bitsadmin-getfilestotal)
  - [bitsadmin getfilestransferred](bitsadmin-getfilestransferred)
  - [bitsadmin gethelpertokenflags](bitsadmin-gethelpertokenflags)
  - [bitsadmin gethelpertokensid](bitsadmin-gethelpertokensid)
  - [bitsadmin gethttpmethod](bitsadmin-gethttpmethod)
  - [bitsadmin getmaxdownloadtime](bitsadmin-getmaxdownloadtime)
  - [bitsadmin getminretrydelay](bitsadmin-getminretrydelay)
  - [bitsadmin getmodificationtime](bitsadmin-getmodificationtime)
  - [bitsadmin getnoprogresstimeout](bitsadmin-getnoprogresstimeout)
  - [bitsadmin getnotifycmdline](bitsadmin-getnotifycmdline)
  - [bitsadmin getnotifyflags](bitsadmin-getnotifyflags)
  - [bitsadmin getnotifyinterface](bitsadmin-getnotifyinterface)
  - [bitsadmin getowner](bitsadmin-getowner)
  - [bitsadmin getpeercachingflags](bitsadmin-getpeercachingflags)
  - [bitsadmin getpriority](bitsadmin-getpriority)
  - [bitsadmin getproxybypasslist](bitsadmin-getproxybypasslist)
  - [bitsadmin getproxylist](bitsadmin-getproxylist)
  - [bitsadmin getproxyusage](bitsadmin-getproxyusage)
  - [bitsadmin getreplydata](bitsadmin-getreplydata)
  - [bitsadmin getreplyfilename](bitsadmin-getreplyfilename)
  - [bitsadmin getreplyprogress](bitsadmin-getreplyprogress)
  - [bitsadmin getsecurityflags](bitsadmin-getsecurityflags)
  - [bitsadmin getstate](bitsadmin-getstate)
  - [bitsadmin gettemporaryname](bitsadmin-gettemporaryname)
  - [bitsadmin gettype](bitsadmin-gettype)
  - [bitsadmin getvalidationstate](bitsadmin-getvalidationstate)
  - [bitsadmin help](bitsadmin-help)
  - [bitsadmin info](bitsadmin-info)
  - [bitsadmin list](bitsadmin-list)
  - [bitsadmin listfiles](bitsadmin-listfiles)
  - [bitsadmin makecustomheaderswriteonly](bitsadmin-makecustomheaderswriteonly)
  - [bitsadmin monitor](bitsadmin-monitor)
  - [bitsadmin nowrap](bitsadmin-nowrap)
  - [bitsadmin peercaching](bitsadmin-peercaching)

    - [bitsadmin peercaching and getconfigurationflags](bitsadmin-peercaching-and-getconfigurationflags)
    - [bitsadmin peercaching and help](bitsadmin-peercaching-and-help)
    - [bitsadmin peercaching and setconfigurationflags](bitsadmin-peercaching-and-setconfigurationflags)

  - [bitsadmin peers](bitsadmin-peers)

    - [bitsadmin peers and clear](bitsadmin-peers-and-clear)
    - [bitsadmin peers and discover](bitsadmin-peers-and-discover)
    - [bitsadmin peers and help](bitsadmin-peers-and-help)
    - [bitsadmin peers and list](bitsadmin-peers-and-list)

  - [bitsadmin rawreturn](bitsadmin-rawreturn)
  - [bitsadmin removeclientcertificate](bitsadmin-removeclientcertificate)
  - [bitsadmin removecredentials](bitsadmin-removecredentials)
  - [bitsadmin replaceremoteprefix](bitsadmin-replaceremoteprefix)
  - [bitsadmin reset](bitsadmin-reset)
  - [bitsadmin resume](bitsadmin-resume)
  - [bitsadmin setaclflag](bitsadmin-setaclflag)
  - [bitsadmin setclientcertificatebyid](bitsadmin-setclientcertificatebyid)
  - [bitsadmin setclientcertificatebyname](bitsadmin-setclientcertificatebyname)
  - [bitsadmin setcredentials](bitsadmin-setcredentials)
  - [bitsadmin setcustomheaders](bitsadmin-setcustomheaders)
  - [bitsadmin setdescription](bitsadmin-setdescription)
  - [bitsadmin setdisplayname](bitsadmin-setdisplayname)
  - [bitsadmin sethelpertoken](bitsadmin-sethelpertoken)
  - [bitsadmin sethelpertokenflags](bitsadmin-sethelpertokenflags)
  - [bitsadmin sethttpmethod](bitsadmin-sethttpmethod)
  - [bitsadmin setmaxdownloadtime](bitsadmin-setmaxdownloadtime)
  - [bitsadmin setminretrydelay](bitsadmin-setminretrydelay)
  - [bitsadmin setnoprogresstimeout](bitsadmin-setnoprogresstimeout)
  - [bitsadmin setnotifycmdline](bitsadmin-setnotifycmdline)
  - [bitsadmin setnotifyflags](bitsadmin-setnotifyflags)
  - [bitsadmin setpeercachingflags](bitsadmin-setpeercachingflags)
  - [bitsadmin setpriority](bitsadmin-setpriority)
  - [bitsadmin setproxysettings](bitsadmin-setproxysettings)
  - [bitsadmin setreplyfilename](bitsadmin-setreplyfilename)
  - [bitsadmin setsecurityflags](bitsadmin-setsecurityflags)
  - [bitsadmin setvalidationstate](bitsadmin-setvalidationstate)
  - [bitsadmin suspend](bitsadmin-suspend)
  - [bitsadmin takeownership](bitsadmin-takeownership)
  - [bitsadmin transfer](bitsadmin-transfer)
  - [bitsadmin util](bitsadmin-util)

    - [bitsadmin util and enableanalyticchannel](bitsadmin-util-and-enableanalyticchannel)
    - [bitsadmin util and getieproxy](bitsadmin-util-and-getieproxy)
    - [bitsadmin util and help](bitsadmin-util-and-help)
    - [bitsadmin util and repairservice](bitsadmin-util-and-repairservice)
    - [bitsadmin util and setieproxy](bitsadmin-util-and-setieproxy)
    - [bitsadmin util and version](bitsadmin-util-and-version)

  - [bitsadmin wrap](bitsadmin-wrap)

- [bootcfg](bootcfg)

  - [bootcfg addsw](bootcfg-addsw)
  - [bootcfg copy](bootcfg-copy)
  - [bootcfg dbg1394](bootcfg-dbg1394)
  - [bootcfg debug](bootcfg-debug)
  - [bootcfg default](bootcfg-default)
  - [bootcfg delete](bootcfg-delete)
  - [bootcfg ems](bootcfg-ems)
  - [bootcfg query](bootcfg-query)
  - [bootcfg raw](bootcfg-raw)
  - [bootcfg rmsw](bootcfg-rmsw)
  - [bootcfg timeout](bootcfg-timeout)

- [break](break)

### C

- [cacls](cacls)
- [call](call)
- [cd](cd)
- [certreq](certreq_1)
- [certutil](certutil)
- [change](change)

  - [change logon](change-logon)
  - [change port](change-port)
  - [change user](change-user)

- [chcp](chcp)
- [chdir](chdir)
- [chglogon](chglogon)
- [chgport](chgport)
- [chgusr](chgusr)
- [chkdsk](chkdsk)
- [chkntfs](chkntfs)
- [choice](choice)
- [cipher](cipher)
- [clean](clean)
- [cleanmgr](cleanmgr)
- [clip](clip)
- [cls](cls)
- [cmd](cmd)
- [cmdkey](cmdkey)
- [cmstp](cmstp)
- [color](color)
- [comp](comp)
- [compact](compact)
- [compact vdisk](compact-vdisk)
- [convert](convert)

  - [convert basic](convert-basic)
  - [convert dynamic](convert-dynamic)
  - [convert gpt](convert-gpt)
  - [convert mbr](convert-mbr)

- [copy](copy)
- [create](create)

  - [create partition efi](create-partition-efi)
  - [create partition extended](create-partition-extended)
  - [create partition logical](create-partition-logical)
  - [create partition msr](create-partition-msr)
  - [create partition primary](create-partition-primary)
  - [create volume mirror](create-volume-mirror)
  - [create volume raid](create-volume-raid)
  - [create volume simple](create-volume-simple)
  - [create volume stripe](create-volume-stripe)

- [cscript](cscript)

### D

- [date](date)
- [dcdiag](dcdiag)
- [dcgpofix](dcgpofix)
- [dcpromo](dcpromo)
- [defrag](defrag)
- [del](del)
- [delete](delete)

  - [delete disk](delete-disk)
  - [delete partition](delete-partition)
  - [delete shadows](delete-shadows)
  - [delete volume](delete-volume)

- [detach vdisk](detach-vdisk)
- [detail](detail)

  - [detail disk](detail-disk)
  - [detail partition](detail-partition)
  - [detail vdisk](detail-vdisk)
  - [detail volume](detail-volume)

- [dfsdiag](dfsdiag)

  - [dfsdiag testdcs](dfsdiag-testdcs)
  - [dfsdiag testdfsconfig](dfsdiag-testdfsconfig)
  - [dfsdiag testdfsintegrity](dfsdiag-testdfsintegrity)
  - [dfsdiag testreferral](dfsdiag-testreferral)
  - [dfsdiag testsites](dfsdiag-testsites)

- [dfsrmig](dfsrmig)
- [diantz](diantz)
- [dir](dir)
- [diskcomp](diskcomp)
- [diskcopy](diskcopy)
- [diskpart](diskpart)
- [diskperf](diskperf)
- [diskraid](diskraid)
- [diskshadow](diskshadow)
- [dispdiag](dispdiag)
- [dnscmd](dnscmd)
- [doskey](doskey)
- [driverquery](driverquery)
- [dtrace](dtrace)

### E

- [echo](echo)
- [edit](edit)
- [endlocal](endlocal)
- [end restore](end-restore)
- [erase](erase)
- [eventcreate](eventcreate)
- [Evntcmd](evntcmd)
- [exec](exec)
- [exit](exit)
- [expand](expand)
- [expand vdisk](expand-vdisk)
- [expose](expose)
- [extend](extend)
- [extract](extract)

### F

- [fc](fc)
- [filesystems](filesystems)
- [find](find)
- [findstr](findstr)
- [finger](finger)
- [flattemp](flattemp)
- [fondue](fondue)
- [for](for)
- [forfiles](forfiles)
- [format](format)
- [freedisk](freedisk)
- [fsutil](fsutil)

  - [fsutil 8dot3name](fsutil-8dot3name)
  - [fsutil behavior](fsutil-behavior)
  - [fsutil devdrv](fsutil-devdrv)
  - [fsutil dirty](fsutil-dirty)
  - [fsutil file](fsutil-file)
  - [fsutil fsinfo](fsutil-fsinfo)
  - [fsutil hardlink](fsutil-hardlink)
  - [fsutil objectid](fsutil-objectid)
  - [fsutil quota](fsutil-quota)
  - [fsutil repair](fsutil-repair)
  - [fsutil reparsepoint](fsutil-reparsepoint)
  - [fsutil resource](fsutil-resource)
  - [fsutil sparse](fsutil-sparse)
  - [fsutil tiering](fsutil-tiering)
  - [fsutil transaction](fsutil-transaction)
  - [fsutil usn](fsutil-usn)
  - [fsutil volume](fsutil-volume)
  - [fsutil wim](fsutil-wim)

- [ftp](ftp)

  - [ftp append](ftp-append)
  - [ftp ascii](ftp-ascii)
  - [ftp bell](ftp-bell_1)
  - [ftp binary](ftp-binary)
  - [ftp bye](ftp-bye)
  - [ftp cd](ftp-cd)
  - [ftp close](ftp-close_1)
  - [ftp debug](ftp-debug)
  - [ftp delete](ftp-delete)
  - [ftp dir](ftp-dir)
  - [ftp disconnect](ftp-disconnect_1)
  - [ftp get](ftp-get)
  - [ftp glob](ftp-glob_1)
  - [ftp hash](ftp-hash_1)
  - [ftp lcd](ftp-lcd)
  - [ftp literal](ftp-literal_1)
  - [ftp ls](ftp-ls_1)
  - [ftp mget](ftp-mget)
  - [ftp mkdir](ftp-mkdir)
  - [ftp mls](ftp-mls_1)
  - [ftp mput](ftp-mput_1)
  - [ftp open](ftp-open_1)
  - [ftp prompt](ftp-prompt_1)
  - [ftp put](ftp-put)
  - [ftp pwd](ftp-pwd_1)
  - [ftp quit](ftp-quit)
  - [ftp quote](ftp-quote)
  - [ftp recv](ftp-recv)
  - [ftp remotehelp](ftp-remotehelp_1)
  - [ftp rename](ftp-rename)
  - [ftp rmdir](ftp-rmdir)
  - [ftp send](ftp-send_1)
  - [ftp status](ftp-status)
  - [ftp trace](ftp-trace_1)
  - [ftp type](ftp-type)
  - [ftp user](ftp-user)
  - [ftp verbose](ftp-verbose_1)
  - [ftp mdelete](ftp.mdelete_1)
  - [ftp mdir](ftp.mdir)

- [ftype](ftype)
- [fveupdate](fveupdate)

### G

- [getmac](getmac)
- [gettype](gettype)
- [goto](goto)
- [gpfixup](gpfixup)
- [gpresult](gpresult)
- [gpt](gpt)
- [gpupdate](gpupdate)
- [graftabl](graftabl)

### H

- [help](help)
- [helpctr](helpctr)
- [hostname](hostname)

### I

- [icacls](icacls)
- [if](if)
- [import (shadowdisk)](import)
- [import (diskpart)](import_1)
- [inactive](inactive)
- [ipconfig](ipconfig)
- [ipxroute](ipxroute)
- [irftp](irftp)

### J

- [jetpack](jetpack)

### K

- [klist](klist)
- [ksetup](ksetup)

  - [ksetup addenctypeattr](ksetup-addenctypeattr)
  - [ksetup addhosttorealmmap](ksetup-addhosttorealmmap)
  - [ksetup addkdc](ksetup-addkdc)
  - [ksetup addkpasswd](ksetup-addkpasswd)
  - [ksetup addrealmflags](ksetup-addrealmflags)
  - [ksetup changepassword](ksetup-changepassword)
  - [ksetup delenctypeattr](ksetup-delenctypeattr)
  - [ksetup delhosttorealmmap](ksetup-delhosttorealmmap)
  - [ksetup delkdc](ksetup-delkdc)
  - [ksetup delkpasswd](ksetup-delkpasswd)
  - [ksetup delrealmflags](ksetup-delrealmflags)
  - [ksetup domain](ksetup-domain)
  - [ksetup dumpstate](ksetup-dumpstate)
  - [ksetup getenctypeattr](ksetup-getenctypeattr)
  - [ksetup listrealmflags](ksetup-listrealmflags)
  - [ksetup mapuser](ksetup-mapuser)
  - [ksetup removerealm](ksetup-removerealm)
  - [ksetup server](ksetup-server)
  - [ksetup setcomputerpassword](ksetup-setcomputerpassword)
  - [ksetup setenctypeattr](ksetup-setenctypeattr)
  - [ksetup setrealm](ksetup-setrealm)
  - [ksetup setrealmflags](ksetup-setrealmflags)

- [ktmutil](ktmutil)
- [ktpass](ktpass)

### L

- [label](label)
- [list](list)

  - [list providers](list-providers)
  - [list shadows](list-shadows)
  - [list writers](list-writers)

- [load metadata](load-metadata)
- [lodctr](lodctr)
- [logman](logman)

  - [logman create](logman-create)
  - [logman create alert](logman-create-alert)
  - [logman create api](logman-create-api)
  - [logman create cfg](logman-create-cfg)
  - [logman create counter](logman-create-counter)
  - [logman create trace](logman-create-trace)
  - [logman delete](logman-delete)
  - [logman import and logman export](logman-import-export)
  - [logman query](logman-query)
  - [logman start and logman stop](logman-start-stop)
  - [logman update](logman-update)
  - [logman update alert](logman-update-alert)
  - [logman update api](logman-update-api)
  - [logman update cfg](logman-update-cfg)
  - [logman update counter](logman-update-counter)
  - [logman update trace](logman-update-trace)

- [logoff](logoff)
- [lpq](lpq)
- [lpr](lpr)

### M

- [macfile](macfile)
- [makecab](makecab)
- [manage bde](manage-bde)

  - [manage bde status](manage-bde-status)
  - [manage bde on](manage-bde-on)
  - [manage bde off](manage-bde-off)
  - [manage bde pause](manage-bde-pause)
  - [manage bde resume](manage-bde-resume)
  - [manage bde lock](manage-bde-lock)
  - [manage bde unlock](manage-bde-unlock)
  - [manage bde autounlock](manage-bde-autounlock)
  - [manage bde protectors](manage-bde-protectors)
  - [manage bde tpm](manage-bde-tpm)
  - [manage bde setidentifier](manage-bde-setidentifier)
  - [manage bde forcerecovery](manage-bde-forcerecovery)
  - [manage bde changepassword](manage-bde-changepassword)
  - [manage bde changepin](manage-bde-changepin)
  - [manage bde changekey](manage-bde-changekey)
  - [manage bde keypackage](manage-bde-keypackage)
  - [manage bde upgrade](manage-bde-upgrade)
  - [manage bde wipefreespace](manage-bde-wipefreespace)

- [mapadmin](mapadmin)
- [md](md)
- [merge vdisk](merge-vdisk)
- [mkdir](mkdir)
- [mklink](mklink)
- [mmc](mmc)
- [mode](mode)
- [more](more)
- [mount](mount)
- [mountvol](mountvol)
- [move](move)
- [mqbkup](mqbkup)
- [mqsvc](mqsvc)
- [mqtgsvc](mqtgsvc)
- [msdt](msdt)
- [msg](msg)
- [msiexec](msiexec)
- [msinfo32](msinfo32)
- [mstsc](mstsc)

### N

- [nbtstat](nbtstat)
- [netcfg](netcfg)
- [netdom](netdom)

  - [netdom add](netdom-add)
  - [netdom computername](netdom-computername)
  - [netdom join](netdom-join)
  - [netdom move](netdom-move)
  - [netdom movent4bdc](netdom-movent4bdc)
  - [netdom query](netdom-query)
  - [netdom remove](netdom-remove)
  - [netdom renamecomputer](netdom-renamecomputer)
  - [netdom reset](netdom-reset)
  - [netdom resetpwd](netdom-resetpwd)
  - [netdom trust](netdom-trust)
  - [netdom verify](netdom-verify)

- [net print](net-print)
- [net user](net-user)
- [netsh](netsh)

  - [netsh add](netsh-add)
  - [netsh advfirewall](netsh-advfirewall)
  - [netsh branchcache](netsh-branchcache)
  - [netsh bridge](netsh-bridge)
  - [netsh delete](netsh-delete)
  - [netsh dhcpclient](netsh-dhcpclient)
  - [netsh dnsclient](netsh-dnsclient)
  - [netsh dump](netsh-dump)
  - [netsh exec](netsh-exec)
  - [netsh http](netsh-http)
  - [netsh interface](netsh-interface)
  - [netsh ipsec](netsh-ipsec)
  - [netsh lan](netsh-lan)
  - [netsh mbn](netsh-mbn)
  - [netsh namespace](netsh-namespace)
  - [netsh netio](netsh-netio)
  - [netsh nlm](netsh-nlm)
  - [netsh ras](netsh-ras)
  - [netsh rpc](netsh-rpc)
  - [netsh set](netsh-set)
  - [netsh show](netsh-show)
  - [netsh trace](netsh-trace)
  - [netsh wcn](netsh-wcn)
  - [netsh wfp](netsh-wfp)
  - [netsh winhttp](netsh-winhttp)
  - [netsh winsock](netsh-winsock)
  - [netsh wlan](netsh-wlan)

- [netstat](netstat)
- [nfsadmin](nfsadmin)
- [nfsshare](nfsshare)
- [nfsstat](nfsstat)
- [nlbmgr](nlbmgr)
- [nltest](/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc731935(v=ws.11))
- [nslookup](nslookup)

  - [nslookup exit Command](nslookup-exit-command)
  - [nslookup finger Command](nslookup-finger-command)
  - [nslookup help](nslookup-help)
  - [nslookup ls](nslookup-ls)
  - [nslookup lserver](nslookup-lserver)
  - [nslookup root](nslookup-root)
  - [nslookup server](nslookup-server)
  - [nslookup set](nslookup-set)
  - [nslookup set all](nslookup-set-all)
  - [nslookup set class](nslookup-set-class)
  - [nslookup set d2](nslookup-set-d2)
  - [nslookup set debug](nslookup-set-debug)
  - [nslookup set domain](nslookup-set-domain)
  - [nslookup set port](nslookup-set-port)
  - [nslookup set querytype](nslookup-set-querytype)
  - [nslookup set recurse](nslookup-set-recurse)
  - [nslookup set retry](nslookup-set-retry)
  - [nslookup set root](nslookup-set-root)
  - [nslookup set search](nslookup-set-search)
  - [nslookup set srchlist](nslookup-set-srchlist)
  - [nslookup set timeout](nslookup-set-timeout)
  - [nslookup set type](nslookup-set-type)
  - [nslookup set vc](nslookup-set-vc)
  - [nslookup view](nslookup-view)

- [ntbackup](ntbackup)
- [ntcmdprompt](ntcmdprompt)
- [ntfrsutl](ntfrsutl)

### O

- [offline](offline)

  - [offline disk](offline-disk)
  - [offline volume](offline-volume)

- [online](online)

  - [online disk](online-disk)
  - [online volume](online-volume)

- [openfiles](openfiles)

### P

- [pagefileconfig](pagefileconfig)
- [path](path)
- [pathping](pathping)
- [pause](pause)
- [pbadmin](pbadmin)
- [pentnt](pentnt)
- [perfmon](perfmon)
- [ping](ping)
- [pktmon](pktmon)
- [pnpunattend](pnpunattend)
- [pnputil](pnputil)
- [popd](popd)
- [powershell](powershell)
- [powershell ise](powershell_ise)
- [print](print)
- [prncnfg](prncnfg)
- [prndrvr](prndrvr)
- [prnjobs](prnjobs)
- [prnmngr](prnmngr)
- [prnport](prnport)
- [prnqctl](prnqctl)
- [prompt](prompt)
- [pubprn](pubprn)
- [pushd](pushd)
- [pushprinterconnections](pushprinterconnections)
- [pwlauncher](pwlauncher)
- [pwsh](/en-us/powershell/module/microsoft.powershell.core/about/about_pwsh)

### Q

- [qappsrv](qappsrv)
- [qprocess](qprocess)
- [query](query)

  - [query process](query-process)
  - [query session](query-session)
  - [query termserver](query-termserver)
  - [query user](query-user)

- [quser](quser)
- [qwinsta](qwinsta)

### R

- [rd](rd)
- [rdpsign](rdpsign)
- [recover](recover)
- [recover disk group](recover_1)
- [refsutil](refsutil)

  - [refsutil compression](refsutil-compression)
  - [refsutil dedup](refsutil-dedup)
  - [refsutil fixboot](refsutil-fixboot)
  - [refsutil iometrics](refsutil-iometrics)
  - [refsutil leak](refsutil-leak)
  - [refsutil salvage](refsutil-salvage)
  - [refsutil streamsnapshot](refsutil-streamsnapshot)
  - [refsutil triage](refsutil-triage)

- [reg](reg)

  - [reg add](reg-add)
  - [reg compare](reg-compare)
  - [reg copy](reg-copy)
  - [reg delete](reg-delete)
  - [reg export](reg-export)
  - [reg import](reg-import)
  - [reg load](reg-load)
  - [reg query](reg-query)
  - [reg restore](reg-restore)
  - [reg save](reg-save)
  - [reg unload](reg-unload)

- [regini](regini)
- [regsvr32](regsvr32)
- [relog](relog)
- [rem](rem)
- [remove](remove)
- [ren](ren)
- [rename](rename)
- [repadmin](/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc770963(v=ws.11))
- [repair](repair)

  - [repair bde](repair-bde)

- [replace](replace)
- [rescan](rescan)
- [reset](reset)

  - [reset session](reset-session)

- [retain](retain)
- [revert](revert)
- [rexec](rexec)
- [risetup](risetup)
- [rmdir](rmdir)
- [robocopy](robocopy)
- [route ws2008](route_ws2008)
- [rpcinfo](rpcinfo)
- [rpcping](rpcping)
- [rsh](rsh)
- [rundll32](rundll32)
- [rundll32 printui](rundll32-printui)
- [rwinsta](rwinsta)

### S

- [san](san)
- [sc config](sc-config)
- [sc create](sc-create)
- [sc delete](sc-delete)
- [sc query](sc-query)
- [schtasks](schtasks)
- [scwcmd](scwcmd)

  - [scwcmd analyze](scwcmd-analyze)
  - [scwcmd configure](scwcmd-configure)
  - [scwcmd register](scwcmd-register)
  - [scwcmd rollback](scwcmd-rollback)
  - [scwcmd transform](scwcmd-transform)
  - [scwcmd view](scwcmd-view)

- [secedit](secedit)

  - [secedit analyze](secedit-analyze)
  - [secedit configure](secedit-configure)
  - [secedit export](secedit-export)
  - [secedit generaterollback](secedit-generaterollback)
  - [secedit import](secedit-import)
  - [secedit validate](secedit-validate)

- [select](select)

  - [select disk](select-disk)
  - [select partition](select-partition)
  - [select vdisk](select-vdisk)
  - [select volume](select-volume)

- [serverceipoptin](serverceipoptin)
- [servermanagercmd](servermanagercmd)
- [serverweroptin](serverweroptin)
- [set environmental variables](set_1)
- [set shadow copy](set)

  - [set context](set-context)
  - [set id](set-id)
  - [setlocal](setlocal)
  - [set metadata](set-metadata)
  - [set option](set-option)
  - [set verbose](set-verbose)

- [setlocal](setlocal)
- [setspn](setspn)
- [setx](setx)
- [sfc](sfc)
- [shadow](shadow)
- [shift](shift)
- [showmount](showmount)
- [shrink](shrink)
- [shutdown](shutdown)
- [simulate restore](simulate-restore)
- [sort](sort)
- [start](start)
- [subcommand set device](wdsutil-set-device)
- [subcommand set drivergroup](wdsutil-set-drivergroup)
- [subcommand set drivergroupfilter](wdsutil-set-drivergroupfilter)
- [subcommand set driverpackage](wdsutil-set-driverpackage)
- [subcommand set image](wdsutil-set-image)
- [subcommand set imagegroup](wdsutil-set-imagegroup)
- [subcommand set server](wdsutil-set-server)
- [subcommand set transportserver](wdsutil-set-transportserver)
- [subcommand set multicasttransmission](wdsutil-start-multicasttransmission)
- [subcommand start namespace](wdsutil-start-namespace)
- [subcommand start server](wdsutil-start-server)
- [subcommand start transportserver](wdsutil-start-transportserver)
- [subcommand stop server](wdsutil-stop-server)
- [subcommand stop transportserver](wdsutil-stop-transportserver)
- [subst](subst)
- [sxstrace](sxstrace)
- [sysocmgr](sysocmgr)
- [systeminfo](systeminfo)

### T

- [takeown](takeown)
- [tapicfg](tapicfg)
- [taskkill](taskkill)
- [tasklist](tasklist)
- [tcmsetup](tcmsetup)
- [telnet](telnet)

  - [telnet close](telnet-close)
  - [telnet display](telnet-display)
  - [telnet open](telnet-open)
  - [telnet quit](telnet-quit)
  - [telnet send](telnet-send)
  - [telnet set](telnet-set)
  - [telnet status](telnet-status)
  - [telnet unset](telnet-unset)

- [tftp](tftp)
- [time](time)
- [timeout](timeout)
- [title](title)
- [tlntadmn](tlntadmn)
- [tpmtool](tpmtool)
- [tpmvscmgr](tpmvscmgr)
- [tracerpt](tracerpt)
- [tracert](tracert)
- [tree](tree)
- [tscon](tscon)
- [tsdiscon](tsdiscon)
- [tsecimp](tsecimp)
- [tskill](tskill)
- [tsprof](tsprof)
- [type](type)
- [typeperf](typeperf)
- [tzutil](tzutil)

### U

- [unexpose](unexpose)
- [uniqueid](uniqueid)
- [unlodctr](unlodctr)

### V

- [ver](ver)
- [verifier](verifier)
- [verify](verify)
- [vol](vol)
- [vssadmin](vssadmin)

  - [vssadmin delete shadows](vssadmin-delete-shadows)
  - [vssadmin list shadows](vssadmin-list-shadows)
  - [vssadmin list writers](vssadmin-list-writers)
  - [vssadmin resize shadowstorage](vssadmin-resize-shadowstorage)

### W

- [waitfor](waitfor)
- [wbadmin](wbadmin)

  - [wbadmin delete catalog](wbadmin-delete-catalog)
  - [wbadmin delete systemstatebackup](wbadmin-delete-systemstatebackup)
  - [wbadmin disable backup](wbadmin-disable-backup)
  - [wbadmin enable backup](wbadmin-enable-backup)
  - [wbadmin get disks](wbadmin-get-disks)
  - [wbadmin get items](wbadmin-get-items)
  - [wbadmin get status](wbadmin-get-status)
  - [wbadmin get versions](wbadmin-get-versions)
  - [wbadmin restore catalog](wbadmin-restore-catalog)
  - [wbadmin start backup](wbadmin-start-backup)
  - [wbadmin start recovery](wbadmin-start-recovery)
  - [wbadmin start sysrecovery](wbadmin-start-sysrecovery)
  - [wbadmin start systemstatebackup](wbadmin-start-systemstatebackup)
  - [wbadmin start systemstaterecovery](wbadmin-start-systemstaterecovery)
  - [wbadmin stop job](wbadmin-stop-job)

- [wdsutil](wdsutil)
- [wecutil](wecutil)
- [wevtutil](wevtutil)
- [where](where)
- [whoami](whoami)
- [winnt](winnt)
- [winnt32](winnt32)
- [winrs](winrs)
- [winsat mem](winsat-mem)
- [winsat mfmedia](winsat-mfmedia)
- [wmic](wmic)
- [writer](writer)
- [wscript](wscript)

### X

- [xcopy](xcopy)

## Feedback

 Was this page helpful? 

YesNoNo

 Need help with this topic? 

 Want to try using Ask Learn to clarify or guide you through this topic? 

Ask LearnAsk Learn Suggest a fix? 

##  Additional resources 

- Last updated on  2025-07-29
