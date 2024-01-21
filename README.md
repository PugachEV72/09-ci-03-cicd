# Домашнее задание к занятию 9 «Процессы CI/CD» - Пугач Евгений.


---

## `Подготовка к выполнению`

1. Создайте две VM в Yandex Cloud с параметрами: 2CPU 4RAM Centos7.
2. Пропишите в inventory playbook созданные хосты.
3. Добавьте в files файл со своим публичным ключом (id_rsa.pub).
4. Запустите playbook, ожидайте успешного завершения.
5. Проверьте готовность SonarQube через браузер.
6. Зайдите под admin\admin, поменяйте пароль на свой.
7. Проверьте готовность Nexus через бразуер.
8. Подключитесь под admin\admin123, поменяйте пароль, сохраните анонимный доступ.

### Ответ:

Две машины подняты в Yandex Cloud при помощи [TERRAFORM](https://github.com/PugachEV72/09-ci-03-cicd/tree/main/terraform_vms)

![Скриншот 1](https://github.com/PugachEV72/Images/blob/master/2024-01-14_15-48-53.png)

Playbook отработал успешно.

![Скриншот 2](https://github.com/PugachEV72/Images/blob/master/2024-01-14_23-27-59.png)

SonarQube и Nexus готовы к работе.

---


## `Знакомоство с SonarQube`

### Основная часть.

1. Создайте новый проект, название произвольное.
2. Скачайте пакет sonar-scanner, который вам предлагает скачать SonarQube.
3. Сделайте так, чтобы binary был доступен через вызов в shell (или поменяйте переменную PATH, или  
   любой другой, удобный вам способ).
4. Проверьте sonar-scanner --version.
5. Запустите анализатор против кода из директории example с дополнительным ключом `-Dsonar.coverage.exclusions=fail.py`.
6. Посмотрите результат в интерфейсе.
7. Исправьте ошибки, которые он выявил, включая warnings.
8. Запустите анализатор повторно — проверьте, что QG пройдены успешно.
9. Сделайте скриншот успешного прохождения анализа, приложите к решению ДЗ.

### Ответ:

![Скриншот 3](https://github.com/PugachEV72/Images/blob/master/2024-01-15_01-09-09.png)

![Скриншот 4](https://github.com/PugachEV72/Images/blob/master/2024-01-15_01-22-02.png)

---

## `Знакомоство с Nexus`

### Основная часть.

1. В репозиторий maven-public загрузите артефакт с GAV-параметрами:
- groupId: netology;
- artifactId: java;
- version: 8_282;
- classifier: distrib;
- type: tar.gz.
2. В него же загрузите такой же артефакт, но с version: 8_102.
3. Проверьте, что все файлы загрузились успешно.
4. В ответе пришлите файл maven-metadata.xml для этого артефекта.

### Ответ:

![Скриншот 5](https://github.com/PugachEV72/Images/blob/master/2024-01-15_02-22-42.png)

![Скриншот 6](https://github.com/PugachEV72/Images/blob/master/2024-01-15_22-37-16.png)

Ссылка на файл [maven-metadata.xml](https://github.com/PugachEV72/09-ci-03-cicd/blob/main/mvn/maven-metadata.xml)

---

## `Знакомство с Maven`

## Подготовка к выполнению

1. Скачайте дистрибутив с maven.
2. Разархивируйте, сделайте так, чтобы binary был доступен через вызов в shell (или поменяйте  
   переменную PATH, или любой другой, удобный вам способ).
3. Удалите из apache-maven-<version>/conf/settings.xml упоминание о правиле, отвергающем HTTP- соединение —  
   раздел mirrors —> id: my-repository-http-unblocker.
4. Проверьте mvn --version.
5. Заберите директорию mvn с pom.

## Основная часть

1. Поменяйте в pom.xml блок с зависимостями под ваш артефакт из первого пункта задания для Nexus.
2. Запустите команду mvn package в директории с pom.xml, ожидайте успешного окончания.
3. Проверьте директорию ~/.m2/repository/, найдите ваш артефакт.
4. В ответе пришлите исправленный файл pom.xml.

### Ответ:

![Скриншот 5](https://github.com/PugachEV72/Images/blob/master/2024-01-21_13-39-44.png)

Ссылка на файл [pom.xml](https://github.com/PugachEV72/09-ci-03-cicd/blob/main/mvn/pom.xml)

---

