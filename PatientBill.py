import PatientClass as pat
import ProcedureClass as proc

def main():

    patient = pat.Patient(1, "Matt Jones", "123 Main st, Waco Tx 76706", "254-555-7415",True)

    proc1 = proc.Procedure("Physical Exam","2/15/2022","Dr. Irvine",250,1)
    proc2 = proc.Procedure("MRI","2/15/2022","Dr. Hamilton",1500,1)
    proc3 = proc.Procedure("CT Scan","2/17/2022","Dr. Drey",1200,2)

    procs = [proc1,proc2,proc3]

    print("*** Patient Bill ***")
    print("Name:",patient.get_name())
    print("Address:",patient.get_address())
    print("Phone:",patient.get_phone())

    totalCharge = 0

    for x in procs:

        if x.get_id() == patient.get_id():

            charge = x.get_chrage()
            totalCharge += charge
            print("\n")
            print("Procedure:",x.get_name())
            print("Date:",x.get_date())
            print("Practitioner:",x.get_practitioner())
            print("Charge: ${:,.2f}".format(charge))

    if patient.get_vet() == True:
        totalCharge = totalCharge * .6
        
    print("\nTotal Charges: ${:,.2f}".format(totalCharge))


main()

