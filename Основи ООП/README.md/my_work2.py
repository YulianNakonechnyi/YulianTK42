
class MyName:
    """Опис класу / Документація
    """
    total_names = 0  # Class Variable

    def __init__(self, name=None) -> None:
        self.name = name if name is not None else self.anonymous_user().name  # Class attributes / Instance variables
        MyName.total_names += 1  # modify class variable
        self.my_id = self.total_names

    @property
    def whoami(self):
        """Class property
        return: повертаємо ім'я
        """
        return f"My name is {self.name}"

    @property
    def my_email(self) -> str:
        """Class property
        return: повертаємо емейл
        """
        return self.create_email()

    def create_email(self) -> str:
        """Instance method
        """
        return f"{self.name}@itcollege.lviv.ua"

    @classmethod
    def anonymous_user(cls):
        """Class method
        """
        return cls("Anonymous")

    @staticmethod
    def say_hello(message="Hello to everyone!"):
        """Static method
        """
        return f"You say: {message}"

    def count_letters_in_name(self) -> int:
        """Instance method
        return: кількість букв в імені
        """
        return len(self.name)


print("Let's Start!")

# Додано ім'я "Yulian"
names = ("Bohdan", "Marta", "Yulian", None)
all_names = {name: MyName(name) for name in names}

for name, me in all_names.items():
    print(f"""{">*<"*20}
This is object: {me} 
This is object attribute: {me.name} / {me.my_id}
This is {type(MyName.whoami)}: {me.whoami} / {me.my_email}
This is {type(me.create_email)} call: {me.create_email()}
This is static {type(MyName.say_hello)} with defaults: {me.say_hello()} 
This is class variable {type(MyName.total_names)}: from class {MyName.total_names} / from object {me.total_names}
This is instance method count_letters_in_name: {me.count_letters_in_name()} letters in the name
{"<*>"*20}""")

print(f"We are done. We create {me.total_names} names! ??? Why {MyName.total_names}?")


