#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <regex>
#include <set>
#include <algorithm>

int main() {

    std::ifstream file("/home/kingston/repos/LLM/the-verdict.txt");
    if (!file.is_open()) {
        std::cerr << "Error: Could not open file." << std::endl;
        return 1;
    }
    std::string raw_text((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    file.close();
    std::regex pattern(R"([,.:;?_!"()\']|--|\s)");
    std::sregex_token_iterator it(raw_text.begin(), raw_text.end(), pattern, -1);
    std::sregex_token_iterator end;
    std::vector<std::string> preprocessed;
    for (; it != end; ++it) {
        std::string item = *it;
        item.erase(0, item.find_first_not_of(" \t\n\r"));
        item.erase(item.find_last_not_of(" \t\n\r") + 1);
        if (!item.empty()) {
            preprocessed.push_back(item);
        }
    }
    std::set<std::string> unique_words(preprocessed.begin(), preprocessed.end());
    std::cout << "Vocabulary size: " << unique_words.size() << std::endl;
    return 0;
}
