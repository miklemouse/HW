#include <string>
#include <set>
#include <fstream>
#include <sstream>
#include <iostream> // debug


void addToSet(std::set<int> &listOfEntries,
              const std::string &commArgument)
{
    try
    {
        std::istringstream ss(commArgument);
        std::string right, left;
        std::getline(ss, right, '-');
        std::getline(ss, left, '-');
        for (int i = std::stoi(right); i <= std::stoi(left); ++i)
            listOfEntries.insert(i);
    }
    catch (const std::invalid_argument &_)
    {
        listOfEntries.insert(std::stoi(commArgument));
    }
}

void extractCells(const std::string &row, std::ostream &ostream,
                  const std::set<int> &colIndices)
{
    std::string cell;
    std::istringstream rowStream(row);
    for (int col = 0; std::getline(rowStream, cell, ','); ++col)
    {
        if (colIndices.find(col) != colIndices.end())
        {
            if (col > 0)
                ostream << ",";
            ostream << cell;
        }
    }
}

void extractColumns(std::istream &istream, std::ostream &ostream,
                    const std::set<int> &colIndices)
{
    std::string row;
    while (std::getline(istream, row))
    {
        extractCells(row, ostream, colIndices);
        ostream << "\n";
    }
}


int main(int argc, char *argv[])
{
    std::ifstream inputFile(argv[1]);
    std::ofstream outputFile(argv[argc - 1]);

    std::set<int> colsToExtract;
    for (int i = 2; i < argc - 1; ++i)
    {
        std::string strColNum(argv[i]);
        addToSet(colsToExtract, strColNum);
    }

    extractColumns(inputFile, outputFile, colsToExtract);

    return 0;
}
