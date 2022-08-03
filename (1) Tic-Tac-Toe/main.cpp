#include <iostream>
using namespace std;

// ============================================================

const char MAXROW = 3;
const char MAXCOL = 3;

// ============================================================

class Board {
public:
    Board();
    void displayBoard();
    void turnHandling();
    void promptPlayerOne();
    void promptPlayerTwo();
    bool checkWinPlayerOne();
    bool checkWinPlayerTwo();
    
private:
    char m_grid[MAXROW][MAXCOL];
};

// ============================================================

Board::Board() {
    int ascii = 0;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            m_grid[i][j] = 49 + ascii;
            ascii++;
        }
    }
}

void Board::displayBoard() {
    cout << "+---+---+---+" << endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << "| " << m_grid[i][j] << " ";
        }
        cout << "|" << endl;
    }
    cout << "+---+---+---+" << endl;
}

void Board::promptPlayerOne() {
    int choice1 = 0;
    cout << "Player 1: Please choose a number on the grid: ";
    cin >> choice1;
    for (int row = 0; row < 3; row++) {
        for (int col = 0; col < 3; col++) {
            if (m_grid[row][col] == 48 + choice1) {
                m_grid[row][col] = 88;
                displayBoard();
                return;
            }
        }
    }
    cout << "Invalid Placement: Please try again." << endl;
    promptPlayerOne();
}

void Board::promptPlayerTwo() {
    int choice2 = 0;
    cout << "Player 2: Please choose a number on the grid: ";
    cin >> choice2;
    
    for (int row = 0; row < 3; row++) {
        for (int col = 0; col < 3; col++) {
            if (m_grid[row][col] == 48 + choice2) {
                m_grid[row][col] = 89;
                displayBoard();
                return;
            }
        }
    }
    
    cout << "Invalid Placement: Please try again." << endl;
    promptPlayerTwo();
    
}


void Board::turnHandling() {
    int i = 0;
    while (i < 9) {
        cout << endl;
        cout << "Turn: " << i + 1 << endl;;
        promptPlayerOne();
        i++;
        
        if (checkWinPlayerOne()) {
            cout << endl;
            cout << "Player 1 has won!" << endl << endl;
            break;
        }
        
        if (i == 9) {
            cout << endl;
            cout << "Tie game!" << endl << endl;
            break;
        }
        
        cout << endl;
        cout << "Turn: " << i + 1 << endl;
        promptPlayerTwo();
        i++;
        
        if (checkWinPlayerTwo()) {
            cout << endl;
            cout << "Player 1 has won!" << endl << endl;
        }
    }
}

bool Board::checkWinPlayerOne() {
    if (m_grid[0][0] == 88 && m_grid[0][1] == 88 && m_grid[0][2] == 88)
        return true;
    else if (m_grid[1][0] == 88 && m_grid[1][1] == 88 && m_grid[1][2] == 88)
        return true;
    else if (m_grid[2][0] == 88 && m_grid[2][1] == 88 && m_grid[2][2] == 88)
        return true;
    else if (m_grid[0][0] == 88 && m_grid[1][0] == 88 && m_grid[2][0] == 88)
        return true;
    else if (m_grid[0][1] == 88 && m_grid[1][1] == 88 && m_grid[2][1] == 88)
        return true;
    else if (m_grid[0][0] == 88 && m_grid[1][1] == 88 && m_grid[2][2] == 88)
        return true;
    else if (m_grid[0][2] == 88 && m_grid[1][2] == 88 && m_grid[2][2] == 88)
        return true;
    else if (m_grid[2][0] == 88 && m_grid[1][1] == 88 && m_grid[0][2] == 88)
        return true;
    else
        return false;
}

bool Board::checkWinPlayerTwo() {
    if (m_grid[0][0] == 89 && m_grid[0][1] == 89 && m_grid[0][2] == 89)
        return true;
    else if (m_grid[1][0] == 89 && m_grid[1][1] == 89 && m_grid[1][2] == 89)
        return true;
    else if (m_grid[2][0] == 89 && m_grid[2][1] == 89 && m_grid[2][2] == 89)
        return true;
    else if (m_grid[0][0] == 89 && m_grid[1][0] == 89 && m_grid[2][0] == 89)
        return true;
    else if (m_grid[0][1] == 89 && m_grid[1][1] == 89 && m_grid[2][1] == 89)
        return true;
    else if (m_grid[0][2] == 89 && m_grid[1][2] == 89 && m_grid[2][2] == 89)
        return true;
    else if (m_grid[0][0] == 89 && m_grid[1][1] == 89 && m_grid[2][2] == 89)
        return true;
    else if (m_grid[2][0] == 89 && m_grid[1][1] == 89 && m_grid[0][2] == 89)
        return true;
    else
        return false;
}
        

// ============================================================

int main() {
    cout << "Player 1: X" << endl;
    cout << "Player 2: Y" << endl;
    
    Board a;
    a.displayBoard();
    a.turnHandling();
    
    return 0;
}
