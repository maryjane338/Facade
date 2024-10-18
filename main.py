class Security:

    def start_security_mode(self):
        print('Система охраны включена.')

    def stop_security_mode(self):
        print('Система охраны выключена.')


class Cctv:

    def start_cctv(self):
        print('Видеонаблюдение включено.')

    def stop_cctv(self):
        print('Выдеонаблюдение выключено.')


class AccessControl:

    def start_access_control(self):
        print('Предоставлен контроль доступа.')

    def stop_access_control(self):
        print('Лишение прав контроля доступа.')


class Alarm:

    def start_alarm(self):
        print('Сигнализация включена.')

    def stop_alarm(self):
        print('Сигнализация выключена.')


class SecuritySystemFacade:

    def __init__(self):
        self.security = Security()
        self.cctv = Cctv()
        self.access = AccessControl()
        self.alarm = Alarm()

    def start_security_system(self):
        print('ОБЕСПЕЧЕНИЕ ДОМАШНЕЙ БЕЗОПАСНОСТИ...')
        self.security.start_security_mode()
        self.cctv.start_cctv()
        self.access.start_access_control()
        self.alarm.start_alarm()

    def stop_security_system(self):
        print('ОТКЛЮЧЕНИЕ ДОМАШНЕЙ БЕЗОПАСНОСТИ...')
        self.security.stop_security_mode()
        self.cctv.stop_cctv()
        self.access.stop_access_control()
        self.alarm.stop_alarm()


facade = SecuritySystemFacade()
selector = input('Вкл/Выкл Системы домашней безопасности: ')
if 'вкл' or 'ВКЛ' or 'Вкл' in selector:
    facade.start_security_system()
elif 'выкл' or 'ВЫКЛ' or 'Выкл' in selector:
    facade.stop_security_system()
else:
    print('Повторите попытку.')
