from union_find.account_merge.union_find_account import unionFind
from collections import defaultdict

def accounts_merge(accounts):
    uf = unionFind(len(accounts))
    email_mappings = dict()
    for i, account in enumerate(accounts):
        emails = account[1:]
        for email in emails:
            if email in email_mappings:
                if account[0] != accounts[email_mappings[email]][0]:
                    return
                uf.union(email_mappings[email], i) 
            email_mappings[email] = i
    merged_accounts = defaultdict(list)
    for email, id in email_mappings.items():
        merged_accounts[uf.find(id)].append(email)

    merged_accounts_list = []
    for parent, emails in merged_accounts.items():
        merged_accounts_list.append([accounts[parent][0]]+sorted(emails))
    return merged_accounts_list




def main():
    all_accounts = [[["Emma", "emma@mail.com", "emma_work@mail.com"], ["Bob", "bob_home@mail.com", "bob123@mail.com"], ["Emma", "emma_art@mail.com", "emma_work@mail.com"], ["Bob", "bob321@mail.com"]],
                    [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]],
                    [["Sarah", "sarah@mail.com", "sh@mail.com"],["Sarah", "sarah1@mail.com", "sarahh@mail.com"], ["Sarah", "sh3@mail.com"]],
                    [["Alice", "alice@mail.com"], ["Alice", "alice_alice@mail.com", "alice@mail.com"], ["Alice", "alice@mail.com", "alice123@mail.com", "aalicee@mail.com"]],
                    [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]]
    
    for i in range(len(all_accounts)):
        print(i+1, ".\tAccounts: \n\t[", sep="")
        for a in all_accounts[i]:
            print("\t",a)
        print("\t]")
        
        merged = accounts_merge(all_accounts[i])
        
        if(merged == None):
            print("Error!\nAccounts sharing some email(s) should have the same names.")
            return

        print("\n\tMerged accounts: \n\t[")
        for m in merged:
            print("\t",m)
        print("\t]")
        print("-" * 100)

if __name__ == '__main__':
        main()