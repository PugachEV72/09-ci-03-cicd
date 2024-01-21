INFO: Scanner configuration file: /root/09-ci-03-cicd/sonar-scanner/sonar-scanner-5.0.1.3006-linux/conf/sonar-scanner.properties
INFO: Project root configuration file: NONE
INFO: SonarScanner 5.0.1.3006
INFO: Java 17.0.7 Eclipse Adoptium (64-bit)
INFO: Linux 5.10.0-26-amd64 amd64
INFO: User cache: /root/.sonar/cache
INFO: Analyzing on SonarQube server 9.1.0
INFO: Default locale: "en_US", source code encoding: "UTF-8"
INFO: Load global settings
INFO: Load global settings (done) | time=99ms
INFO: Server id: 9CFC3560-AY0JpCAgeBTLf3Yto1Ba
INFO: User cache: /root/.sonar/cache
INFO: Load/download plugins
INFO: Load plugins index
INFO: Load plugins index (done) | time=79ms
INFO: Load/download plugins (done) | time=134ms
INFO: Process project properties
INFO: Process project properties (done) | time=6ms
INFO: Execute project builders
INFO: Execute project builders (done) | time=1ms
INFO: Project key: Netology
INFO: Base dir: /root/09-ci-03-cicd/example
INFO: Working dir: /root/09-ci-03-cicd/example/.scannerwork
INFO: Load project settings for component key: 'Netology'
INFO: Load project settings for component key: 'Netology' (done) | time=28ms
INFO: Load quality profiles
INFO: Load quality profiles (done) | time=86ms
INFO: Load active rules
INFO: Load active rules (done) | time=2148ms
INFO: Indexing files...
INFO: Project configuration:
INFO: 2 files indexed
INFO: 0 files ignored because of scm ignore settings
INFO: Quality profile for py: Sonar way
INFO: ------------- Run sensors on module Netology
INFO: Load metrics repository
INFO: Load metrics repository (done) | time=37ms
INFO: Sensor Python Sensor [python]
WARN: Your code is analyzed as compatible with python 2 and 3 by default. This will prevent the detection of issues specific to python 2 or python 3. You can get a more precise analysis by setting a python version in your configuration via the parameter "sonar.python.version"
INFO: Starting global symbols computation
INFO: 2 source files to be analyzed
INFO: Load project repositories
INFO: Load project repositories (done) | time=50ms
INFO: 2/2 source files have been analyzed
INFO: Starting rules execution
INFO: 2 source files to be analyzed
INFO: 2/2 source files have been analyzed
INFO: Sensor Python Sensor [python] (done) | time=460ms
INFO: Sensor Cobertura Sensor for Python coverage [python]
INFO: Sensor Cobertura Sensor for Python coverage [python] (done) | time=16ms
INFO: Sensor PythonXUnitSensor [python]
INFO: Sensor PythonXUnitSensor [python] (done) | time=0ms
INFO: Sensor CSS Rules [cssfamily]
INFO: No CSS, PHP, HTML or VueJS files are found in the project. CSS analysis is skipped.
INFO: Sensor CSS Rules [cssfamily] (done) | time=0ms
INFO: Sensor JaCoCo XML Report Importer [jacoco]
INFO: 'sonar.coverage.jacoco.xmlReportPaths' is not defined. Using default locations: target/site/jacoco/jacoco.xml,target/site/jacoco-it/jacoco.xml,build/reports/jacoco/test/jacocoTestReport.xml
INFO: No report imported, no coverage information will be imported by JaCoCo XML Report Importer
INFO: Sensor JaCoCo XML Report Importer [jacoco] (done) | time=2ms
INFO: Sensor C# Project Type Information [csharp]
INFO: Sensor C# Project Type Information [csharp] (done) | time=1ms
INFO: Sensor C# Analysis Log [csharp]
INFO: Sensor C# Analysis Log [csharp] (done) | time=10ms
INFO: Sensor C# Properties [csharp]
INFO: Sensor C# Properties [csharp] (done) | time=1ms
INFO: Sensor JavaXmlSensor [java]
INFO: Sensor JavaXmlSensor [java] (done) | time=0ms
INFO: Sensor HTML [web]
INFO: Sensor HTML [web] (done) | time=2ms
INFO: Sensor VB.NET Project Type Information [vbnet]
INFO: Sensor VB.NET Project Type Information [vbnet] (done) | time=1ms
INFO: Sensor VB.NET Analysis Log [vbnet]
INFO: Sensor VB.NET Analysis Log [vbnet] (done) | time=33ms
INFO: Sensor VB.NET Properties [vbnet]
INFO: Sensor VB.NET Properties [vbnet] (done) | time=0ms
INFO: ------------- Run sensors on project
INFO: Sensor Zero Coverage Sensor
INFO: Sensor Zero Coverage Sensor (done) | time=7ms
INFO: SCM Publisher SCM provider for this project is: git
INFO: SCM Publisher 2 source files to be analyzed
INFO: SCM Publisher 0/2 source files have been analyzed (done) | time=29ms
WARN: Missing blame information for the following files:
WARN:   * -Dsonar.coverage.exclusions=fail.py
WARN:   * fail.py
WARN: This may lead to missing/broken features in SonarQube
INFO: CPD Executor Calculating CPD for 1 file
INFO: CPD Executor CPD calculation finished (done) | time=6ms
INFO: Analysis report generated in 64ms, dir size=107.4 kB
INFO: Analysis report compressed in 11ms, zip size=15.8 kB
INFO: Analysis report uploaded in 53ms
INFO: ANALYSIS SUCCESSFUL, you can browse http://158.160.114.38:9000/dashboard?id=Netology
INFO: Note that you will be able to access the updated dashboard once the server has processed the submitted analysis report
INFO: More about the report processing at http://158.160.114.38:9000/api/ce/task?id=AY0KD_pleBTLf3Yto6Gi
INFO: Analysis total time: 4.338 s
INFO: ------------------------------------------------------------------------
INFO: EXECUTION SUCCESS
INFO: ------------------------------------------------------------------------
INFO: Total time: 5.215s
INFO: Final Memory: 16M/60M
INFO: ------------------------------------------------------------------------
