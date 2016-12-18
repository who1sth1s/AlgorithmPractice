class InterestingParty:

    def __init__(self, first_interested_subjects, second_interested_subjects):

        self.first_interested_subjects = first_interested_subjects
        self.second_interested_subjects = second_interested_subjects

    def best_invitation(self):

        all_interested_subject = self.combine_interested_subject()

        if not all_interested_subject:

            return "Can't equal first interested subject and second interested subject"

        interested_subject_gathering = self.make_interested_subject_gathering(all_interested_subject)
        best_invitation_number = max(interested_subject_gathering.values())

        return 'return : ' + str(best_invitation_number)

    def combine_interested_subject(self):

        for (index, first_interested_subject) in enumerate(self.first_interested_subjects):

            if first_interested_subject == self.second_interested_subjects[index]:

                return False

        all_interested_subject = self.first_interested_subjects + self.second_interested_subjects

        return all_interested_subject

    def make_interested_subject_gathering(self, all_interested_subject):

        interested_subject_gathering = dict()

        for interested_subject in all_interested_subject:

            if interested_subject not in interested_subject_gathering:

                interested_subject_gathering[interested_subject] = all_interested_subject.count(interested_subject)

        return interested_subject_gathering
