class Solution {
public:
    string parseEmail(string email) {
        size_t dotPos = email.find(".");
        size_t atSignPos = email.find("@");
        while (dotPos < atSignPos) {
            email.replace(dotPos, 1, "");
            dotPos = email.find(".");
            atSignPos = email.find("@");
        }
        size_t plusPos = email.find("+");
        atSignPos = email.find("@");
        if (plusPos != string::npos)
            email.replace(plusPos, atSignPos - plusPos, "");
        return email;
    }
    int numUniqueEmails(vector<string>& emails) {
        set<string> uniqueEmails;
        for (vector<string>::iterator it = emails.begin(); it != emails.end(); ++it)         {
            string parsedEmail = parseEmail(*it);
            uniqueEmails.insert(parsedEmail);
        }
        return uniqueEmails.size();
    }
};
