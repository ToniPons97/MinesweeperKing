# MinesweeperKing

I decided to take a break, so I went online to play minesweeper and came across 
this website http://minesweeperonline.com/ and started playing. Then I realized 
there's an import and export function and at that precise moment I just knew 
it was ON.

As it turns out you can import or export the game state as a Base64 encoded 
string. There's data like time, difficulty, every row, every number and every 
mine. It's easy to notice that the negative integers are the mines if you've 
played minesweeper.

After that it was just coding a bit of Selenium to do the rest of the trick.
If you want to try it out, install the dependencies and run scrapper.py.
