#include <stdio.h>

int main()
{
        int x,y,z, treeheight;
        char tree_char = '#';

        // Init program and ask for tree height
        printf("========================\n");
        printf("= Print a Tree Program =\n");
        printf("========================\n");
        printf("Enter a tree height\n> ");

        // Check input that user didn't give 1 as tree height
        do{
                scanf("%d", &treeheight);
                if (treeheight < 2){
                        printf("Please enter a height greater than 1\n> ");
                }
        } while(treeheight < 2);


        // Draw the top of the box based on tree height and width
        // Python print("=" * (treeheight * 2 + 5))
        for (z = 0; z < (treeheight * 2 + 5); z++){
                printf("=");
        }

        // Starts tree on next line
        printf("\n");

        // Draw the Tree (No Stump)!
        // X defines each line and what it contains to make the tree
        for (x = 1; x < treeheight+1; x++) {

                printf("= ");  // makes the outside box wall

                // Adaptive spacing. Treeheight is the radius of the box - the currently filled tree char
                for (y = 0; y < (treeheight - x + 1); y++){
                        printf(" ");
                }

                // Grow the tree
                for (y = 0; y < (x * 2) - 1; y++){
                        printf("%c", tree_char);
                }

                // Adaptive spacing. Treeheight is the radius of the box - the currently filled tree char
                for (y = 0; y < (treeheight - x + 1); y++){
                        printf(" ");
                }

                printf(" =\n");
        }

        // Draw the Stump of the Tree
        // X defines console lines for the tree stump and padding

        // Height < 5 = 1x1 tree stump
        if (treeheight <= 5) {
                for (x = 0; x < 1; x++){

                        // Continue left box wall
                        printf("= ");

                        // Creates space padding
                        for (y = 0; y < treeheight; y++){
                                printf(" ");
                        }
                        // Stump
                        printf("%c", tree_char);

                        // Creates space padding
                        for (y = 0; y < treeheight; y++){
                                printf(" ");
                        }

                        // Continue right box wall
                        printf(" =\n");
                }
        }

        // Height < 5 = 3x2 tree stump
        else if (treeheight <= 10) {
                for (x = 0; x < 2; x++){

                        // Continue left box wall
                        printf("= ");

                        // Creates space padding
                        for (y = 0; y < (treeheight - 1); y++){
                                printf(" ");
                        }
                        // Stump
                        for (y = 0; y < 3; y++){
                                printf("%c", tree_char);
                        }

                        // Creates space padding
                        for (y = 0; y < (treeheight - 1); y++){
                                printf(" ");
                        }

                        // Continue Right box wall
                        printf(" =\n");
                }
        }

        // Height < 5 = 3x4 tree stump
        else {
                for (x = 0; x < 4; x++){

                        // Continue Left box wall
                        printf("= ");

                        // Creates space padding
                        for (y = 0; y < (treeheight - 1); y++){
                                printf(" ");
                        }
                        // Stump
                        for (y = 0; y < 3; y++){
                                printf("%c", tree_char);
                        }

                        // Creates space padding
                        for (y = 0; y < (treeheight - 1); y++){
                                printf(" ");
                        }

                        // Continue right box wall
                        printf(" =\n");
                }
        }

        // Draw the bottom of the box based on tree height and width
        // Python print("=" * (treeheight * 2 + 5))
        for (z = 0; z < (treeheight * 2 + 5); z++){
                printf("=");
        }

        printf("\n");

        return 0;
}