# We are going to create a setting in a office, that different people are busy with different work.
# To deal with different interfaces of different work, we use adaptor pattern to make a common interface.

class Customer_Server(object):
    def __init__(self):
        self.occupation = "Customer Server"

    def get_occupation(self):
        return self.occupation

    def answering_the_phone(self):
        return ("answering the phone")

class Software_Engineer(object):
    def __init__(self):
        self.occupation = "Software Engineer"

    def get_occupation(self):
        return self.occupation

    def adding_new_feature(self):
        return ("adding new feature")

class Test_Engineer(object):
    def __init__(self):
        self.occupation = "Test Engineer"

    def get_occupation(self):
        return self.occupation

    def testing_old_feature(self):
        return ("testing old feature")

class Office_Adapter(object):
    def __init__(self, occupation, **adpated_methods):
        self.occupation = occupation
        self.__dict__.update(adpated_methods)

    def __getattr__(self, attr):
        # All non-adapted calls are passed to the object
        return getattr(self.occupation, attr)

if __name__ == "__main__":
    occupations = []

    customer_service = Customer_Server()
    software_engineer = Software_Engineer()
    test_engineer = Test_Engineer()

    occupations.append(Office_Adapter(customer_service, working=customer_service.answering_the_phone))
    occupations.append(Office_Adapter(software_engineer, working=software_engineer.adding_new_feature))
    occupations.append(Office_Adapter(test_engineer, working=test_engineer.testing_old_feature))

    for occupation in occupations:
        print("%s is %s" % (occupation.get_occupation(), occupation.working()))
