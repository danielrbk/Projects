import java.io.*;
import java.util.*;

/**
 * Created by Daniel on 18-Apr-17.
 */
public class SubCbc {
    static int BLOCK_SIZE = 10;
    static int IV_SIZE = 10;
    String input, init, plainText, cryptedText;
    char[] key;
    boolean[] locked;
    int decryptedCount = 0;
    int lastDecryptedCount = -1;
    PermutationGenerator pg;
    HashMap<Character,Integer> letterCount = new HashMap<Character,Integer>();
    HashSet<Integer> set;
    public static HashSet<String> dict = new HashSet<String>();

    public SubCbc(String input, String key, String init) {
        int rem = input.length() % BLOCK_SIZE;
        if(rem!=0) {
            String toAdd = "";
            for(int i=0; BLOCK_SIZE-rem-i>0; i++) {
                toAdd += (char)0;
            }
            input += toAdd;
        }
        this.input = input;
        if(key=="") {
            key = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
        }
        decryptedCount = 52-8;
        this.key = key.toCharArray();
        locked = new boolean[key.length()];
        for(int i=0; i<8; i++) {
            locked[i] = false;
        }
        for(int i=8; i<52; i++) {
            locked[i] = true;
        }
        this.init = init;
        set = new HashSet<Integer>();
        for(int i=0; i<=51; i++) {
            set.add(i);
        }
        initializeDict();
    }

    public SubCbc(String input, String key, String init, String plainText, String cryptedText) {
        BLOCK_SIZE = 8128;
        IV_SIZE = 8128;
        int rem = input.length() % BLOCK_SIZE;
        if(rem!=0) {
            String toAdd = "";
            for(int i=0; BLOCK_SIZE-rem-i>0; i++) {
                toAdd += (char)0;
            }
            input += toAdd;
        }
        this.input = input;
        if(key=="")
            key = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
        this.key = key.toCharArray();
        locked = new boolean[key.length()];
        for(int i=0; i<key.length(); i++) {
            locked[i] = false;
        }
        this.init = init;
        rem = plainText.length() % BLOCK_SIZE;
        if(rem!=0) {
            String toAdd = "";
            for(int i=0; BLOCK_SIZE-rem-i>0; i++) {
                toAdd += (char)0;
            }
            plainText += toAdd;
        }
        this.plainText = plainText;
        this.cryptedText = cryptedText;
        set = new HashSet<Integer>();
        for(int i=0; i<=51; i++) {
            set.add(i);
        }
        initializeDict();

    }

    public String encrypt() {
        int length = input.length();
        char[] output = new char[length];
        char[] inputArr = input.toCharArray();
        char[] initArr = init.toCharArray();
        int numOfBlocks = length/BLOCK_SIZE;

        for(int i=0; i<IV_SIZE; i++) {
            inputArr[i] = (char)((int)inputArr[i] ^ (int)initArr[i]);
        }

        for(int blockNum=0; blockNum<numOfBlocks; blockNum++) {
            for (int i = 0; i < BLOCK_SIZE; i++)
                output[i + blockNum*BLOCK_SIZE] = mapCharacter(inputArr[i + blockNum*BLOCK_SIZE]);
            if(blockNum+1 == numOfBlocks)
                return String.valueOf(output);
            for(int i=0; i<BLOCK_SIZE; i++) {
                inputArr[i + (blockNum+1)*BLOCK_SIZE] = (char)((int)inputArr[i + (blockNum+1)*BLOCK_SIZE] ^ (int)output[i + blockNum*BLOCK_SIZE]);
            }
        }
        return String.valueOf(output);
    }

    public String decrypt() {
        int length = input.length();
        char[] output = new char[length];
        char[] inputArr = input.toCharArray();
        char[] initArr = init.toCharArray();
        int numOfBlocks = length/BLOCK_SIZE;

        for (int i = 0; i < IV_SIZE; i++)
            output[i] = (char)((int)decryptCharacter(inputArr[i]) ^ (int)(initArr[i]));

        for(int blockNum=1; blockNum<numOfBlocks; blockNum++) {
            for (int i=0; i<BLOCK_SIZE; i++) {
                output[i + blockNum*BLOCK_SIZE] = (char)((int)decryptCharacter(inputArr[i + (blockNum*BLOCK_SIZE)]) ^ (int)(inputArr[i + (blockNum-1)*BLOCK_SIZE]));
            }
         }
        return String.valueOf(output);
    }

    public Character mapCharacter(char c) {
        int charNum = c - 97;
        if (charNum<26 && charNum >= 0)
            return key[charNum];
        charNum = c - 65;
        if (charNum<26 && charNum >= 0)
            return key[charNum+26];
        return c;
    }

    public Character decryptCharacter(char c) {
        for(int i=0; i<key.length; i++) {
            if (i<26 && c == key[i]) {
                return (char)(i+97);
            }
            else if (i>=26 && c == key[i]) {
                return (char)((i-26) + 65);
            }
        }
        return c;
    }
    private void countLetters() {
        popualteDictionary();
        String sol = decrypt();
        for(int i=0; i<sol.length(); i++) {
            letterCount.replace(sol.charAt(i),letterCount.get(sol.charAt(i))+1);
        }
    }

    private int[] calculateFrequencies() {
        int[] frequencies = new int[26];
        for(int i=0; i<26; i++) {
            frequencies[i] = letterCount.get((char)(i+65))+letterCount.get((char)(i+97));
        }
        return frequencies;
    }

    private void popualteDictionary() {
        for(int i=97; i<=122; i++) {
            letterCount.put((char)i,0);
        }
    }

    private String[] decryptBlocks(int fromBlock, int toBlock) {
        int length;
        char encryptedChar;
        char[] decryptedText = new char[(toBlock-fromBlock)*BLOCK_SIZE];
        char[] xordText = new char[(toBlock-fromBlock)*BLOCK_SIZE];
        char[] encryptedText = new char[(toBlock-fromBlock)*BLOCK_SIZE];
        int blockNum = fromBlock;
        while(blockNum<IV_SIZE/BLOCK_SIZE) {
            for(int i=0; i<BLOCK_SIZE; i++) {
                int index = fromBlock * BLOCK_SIZE + i;
                encryptedChar = input.charAt(index);
                encryptedText[index] = encryptedChar;
                encryptedChar = decryptCharacter(encryptedChar);
                xordText[index] = encryptedChar;
                decryptedText[index] = (char)((int)encryptedChar ^ (int)init.charAt(index));
            }
            blockNum++;
        }
        for(;blockNum<toBlock; blockNum++) {
            for(int i=0; i<BLOCK_SIZE; i++) {
                int index = blockNum * BLOCK_SIZE + i;
                int arrIndex = (blockNum-fromBlock)*BLOCK_SIZE + i;
                encryptedChar = input.charAt(index);
                encryptedText[arrIndex] = encryptedChar;
                encryptedChar = decryptCharacter(encryptedChar);
                xordText[arrIndex] = encryptedChar;
                decryptedText[arrIndex] = (char)((int)encryptedChar ^ (int)input.charAt(index-BLOCK_SIZE));
            }
        }
        String[] sol = new String[3];
        sol[0] = String.valueOf(decryptedText);
        sol[1] = String.valueOf(xordText);
        sol[2] = String.valueOf(encryptedText);
        return sol;
    }

    public String plainTextAttack() {
        int fromBlock = 0;
        int toBlock = plainText.length() / BLOCK_SIZE;
        char[] xordText = new char[(toBlock-fromBlock)*BLOCK_SIZE];
        int index;
        while(fromBlock+1<=IV_SIZE/BLOCK_SIZE) {
            for(int i=0; i<BLOCK_SIZE; i++) {
                index = fromBlock * BLOCK_SIZE + i;
                xordText[index] = (char)((int)plainText.charAt(index) ^ (int)init.charAt(index));
            }
            fromBlock++;
        }
        for(int blockNum=fromBlock; blockNum<toBlock; blockNum++) {
            for(int i=0; i<BLOCK_SIZE; i++) {
                index = fromBlock * BLOCK_SIZE + i;
                xordText[index] = (char)((int)plainText.charAt(index) ^ (int)input.charAt(index-BLOCK_SIZE));
            }
        }
        char c;
        int charNum1;
        for(int i=0; i<cryptedText.length(); i++) {
            c = cryptedText.charAt(i);
            if((65<=c && c<=90) || (97<=c && c<=122)) {
                c = xordText[i];
                charNum1 = c - 97;
                if (!(charNum1 < 26 && charNum1 >= 0))
                    charNum1 = c - 65 + 26;
                key[charNum1] = cryptedText.charAt(i);
                if (!locked[charNum1]) {
                    decryptedCount++;
                    locked[charNum1] = true;
                }
            }
        }
        return crackRestKey();
    }

    public String crackRestKey() {
        final long startTime = System.nanoTime();
        long endTime;
        int BLOCKS_PER_RUN = 8128/BLOCK_SIZE;
        int runs = input.length()/(BLOCK_SIZE*BLOCKS_PER_RUN);
        if(runs == 0)
            runs++;
        String[] sol;
        String decryptedText,xordWords, plain;
        String[] words;
        boolean cracked = false;
        boolean change = true;
        boolean testMode = true;
        double succPer, benchmark = 0.5;
        do
        {
            cracked = true;
            if(change)
                guessKey();
            change = true;
            for(int i=0; i<input.length()/(BLOCK_SIZE*BLOCKS_PER_RUN); i++) {
                sol = decryptBlocks(i * BLOCKS_PER_RUN, (i + 1) * BLOCKS_PER_RUN);
                decryptedText = sol[0];
                words = decryptedText.split("[\\p{Punct}\\s]+");
                words = Arrays.copyOfRange(words, 1, words.length - 2);
                succPer = Arrays.stream(words).filter(e -> dict.contains(e.toLowerCase())).count() / ((double) words.length);
                if (succPer < benchmark) {
                    cracked = false;
                    break;
                }
                xordWords = sol[1];
                plain = sol[2];
                int wordNumber = 0;
                String encryptedWord = "";
                String xordWord = "";
                String decryptedWord = "";
                char c;
                for (int letter = 0; letter < xordWords.length(); letter++) {
                    c = decryptedText.charAt(letter);
                    if (c!=',' && c!='.' && c!= ':' && c!='!' && c!=';' && c!='\'' && c!='\"' && c!=' ') {
                        if (decryptedWord!="" && dict.contains(decryptedWord.toLowerCase())) {
                            mapKeyFromWords(encryptedWord, xordWord);
                        }
                        encryptedWord = "";
                        xordWord = "";
                        decryptedWord = "";
                    }
                    else
                        decryptedWord += c;
                    c = xordWords.charAt(letter);
                    if (((c >= 65 && c <= 90) || (c >= 97 && c <= 122))) {
                        encryptedWord += plain.charAt(letter);
                        xordWord += xordWords.charAt(letter);
                    }

                }
            }
            if(cracked) {
                benchmark += 0.05;
                change = false;
                cracked = false;
            }
            endTime = System.nanoTime();
        }
        while(benchmark<0.90 && (endTime-startTime)/1000000<50000);
        return writeKey();
    }

    private String writeKey() {
        int keyLength;
        if(BLOCK_SIZE==10) {
            keyLength = 8;
        }
        else
            keyLength = 52;
        String str = "";
        for(int i=0; i<26 && i<keyLength; i++) {
            str += ((char)(i+97)) + " " + key[i] + "\r\n";
        }
        for(int i=26; i<52 && i<keyLength; i++) {
            str += ((char)(i-26+65)) + " " + key[i] + "\r\n";
        }
        return str;
    }

    private boolean mapKeyFromWords(String encryptedWord, String xordWord) {
        char c;
        int charNum1;
        boolean changed = false;
        for(int i=0; i<xordWord.length(); i++) {
            c = xordWord.charAt(i);
            charNum1 = c - 97;
            if (!(charNum1<26 && charNum1 >= 0))
                charNum1 = c - 65 + 26;
            if(!locked[charNum1]) {
                key[charNum1] = encryptedWord.charAt(i);
                changed = true;
                decryptedCount++;
                if(charNum1==6)
                    changed = true;
                locked[charNum1] = true;
            }
        }
        return changed;
    }

    private void guessKey() {
        char c;
        int charNum1;
        for(int i=0; i<52; i++) {
            if(locked[i]) {
                c = key[i];
                charNum1 = c - 97;
                if (!(charNum1 < 26 && charNum1 >= 0))
                    charNum1 = c - 65 + 26;
                set.remove(charNum1);
            }
        }
        permutate(set.toArray());
    }

    private void permutate(Object[] arr) {
        Integer[] castedArr = new Integer[arr.length];
        for(int i=0; i<castedArr.length; i++) {
            castedArr[i] = (Integer)arr[i];
        }
        if(lastDecryptedCount!=decryptedCount) {
            Arrays.sort(arr);
            pg = new PermutationGenerator(castedArr.clone());
        }
        else {
            castedArr = (Integer[]) pg.nextPermutation();
        }
        lastDecryptedCount = decryptedCount;
        int count =0;
        for(int i=0; i<key.length; i++) {
            if(!locked[i]) {
                if (castedArr[count] >= 26) {
                    castedArr[count] = castedArr[count] - 26 + 65;
                } else {
                    castedArr[count] = castedArr[count] + 97;
                }
                key[i] = (char)((int)castedArr[count]);
                count++;
            }
        }
    }

    private boolean isCracked(String decrytpedText, double benchmark) {
        String[] txt = decrytpedText.split("[\\p{Punct}\\s]+");
        double succPer = Arrays.stream(txt).filter(e -> dict.contains(e.toLowerCase())).count() / ((double)txt.length);
        if(succPer>benchmark)
            return true;
        return false;

    }

    public void initializeDict() {
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(this.getClass().getResourceAsStream("/words.txt")));
            String line = br.readLine();
            while(line!=null) {
                dict.add(line);
                line = br.readLine();
            }

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
    public static void main(String[] args) {
        SubCbc s = new SubCbc("","abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ","0000000000");
        s.mapKeyFromWords("abcd","ZYXW");
        for(int i=0; i<20; i++) {
            s.guessKey();
            System.out.println(Arrays.toString(s.key));
        }
    }

}
