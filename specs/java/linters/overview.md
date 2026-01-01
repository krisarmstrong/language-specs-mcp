# Java Linting Overview

Common Java static analysis tools.

## Checkstyle

Style and coding standard checker.

```xml
<!-- pom.xml -->
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-checkstyle-plugin</artifactId>
    <version>3.3.0</version>
    <configuration>
        <configLocation>checkstyle.xml</configLocation>
    </configuration>
</plugin>
```

## SpotBugs (successor to FindBugs)

Bug pattern detection.

```xml
<plugin>
    <groupId>com.github.spotbugs</groupId>
    <artifactId>spotbugs-maven-plugin</artifactId>
    <version>4.7.3.0</version>
</plugin>
```

## Error Prone

Compile-time bug detection by Google.

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <configuration>
        <compilerArgs>
            <arg>-XDcompilePolicy=simple</arg>
            <arg>-Xplugin:ErrorProne</arg>
        </compilerArgs>
    </configuration>
</plugin>
```

## PMD

Code analysis for bugs, dead code, complexity.

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-pmd-plugin</artifactId>
    <version>3.21.0</version>
</plugin>
```

## SonarQube

Comprehensive code quality platform.

```bash
mvn sonar:sonar \
  -Dsonar.projectKey=myproject \
  -Dsonar.host.url=http://localhost:9000
```
