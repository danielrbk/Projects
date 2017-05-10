import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Main {

    public static void main(String[] args) {
        String[] flags = isolateFlags(args);
        String input = getInput(flags[Flags.INPATH.getIndex()]);
        String key = getKey(flags[Flags.KEYPATH.getIndex()]);
        String init = getInit(flags[Flags.INITPATH.getIndex()]);
        String algo = flags[Flags.ALGORITHM.getIndex()];
        String mode = flags[Flags.ACTION.getIndex()];
        String knownPath = getKnown(flags[Flags.KNOWNPATH.getIndex()]);
        String cryptedPath = getCrypted(flags[Flags.CRYPTEDPATH.getIndex()]);
        writeOutput(flags[Flags.OUTPATH.getIndex()],runAlgorithm(algo,input,key,init,mode,knownPath,cryptedPath));
    }

    public static String readFile(String path, String defaultPath, boolean nullable) {
        if(path == null) {
            if(nullable)
                return "";
            path = defaultPath;
        }
        try {
            return new String(Files.readAllBytes(Paths.get(path)), StandardCharsets.UTF_8);
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }

    public static String getInput(String path) {
        return readFile(path, "/Users/Public/testInput.txt", false);
    }
    public static String getKey(String path) {
        return readFile(path, "/Users/Public/testKey.txt", true);
    }
    public static String getInit(String path) {
        return readFile(path, "/Users/Public/testInit.txt", false);
    }
    public static String getKnown(String path) {
        return readFile(path, "/Users/Public/testKnown.txt", true);
    }
    public static String getCrypted(String path) {
        return readFile(path, "/Users/Public/testCrypted.txt", true);
    }

    public static void writeOutput(String path, String result) {
        if(path == null) {
            path = "/Users/Public/testRes.txt";
        }
        try {
            File f = new File(path);
            f.createNewFile();
            PrintWriter out = new PrintWriter(path);
            out.println(result);
            out.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static String runAlgorithm(String algorithm, String input, String key, String init, String mode, String knownPath, String cryptedPath) {
        switch(mode) {
            case "encryption":
                switch(algorithm) {
                    case "sub_cbc_10":
                        return (new SubCbc(input,key,init)).encrypt();
                    case "sub_cbc_52":
                        return (new SubCbc(input,key,init,"","")).encrypt();
                }
            case "decryption":
                switch(algorithm) {
                    case "sub_cbc_10":
                        return (new SubCbc(input,key,init)).decrypt();
                    case "sub_cbc_52":
                        return (new SubCbc(input,key,init,"","")).decrypt();
                }
            case "attack":
                switch(algorithm) {
                    case "sub_cbc_10":
                        return (new SubCbc(input,"",init)).crackRestKey();
                    case "sub_cbc_52":
                        return (new SubCbc(input,"",init,knownPath,cryptedPath)).plainTextAttack();
                }
            default:
                System.out.println("Unrecognized mode!");
                return null;
        }
    }

    public static String[] isolateFlags(String[] args) {
        String[] arr = new String[Flags.values().length];
        String curr;
        for (int i=0; i<args.length; i++) {
            curr = args[i];
            if(curr.charAt(0) == '-') {
                i++;
                switch(curr) {
                    case "-a":
                        arr[Flags.ALGORITHM.getIndex()] = args[i];
                        break;
                    case "-c":
                        arr[Flags.ACTION.getIndex()] = args[i];
                        break;
                    case "-t":
                        arr[Flags.INPATH.getIndex()] = args[i];
                        break;
                    case "-k":
                        arr[Flags.KEYPATH.getIndex()] = args[i];
                        break;
                    case "-v":
                        arr[Flags.INITPATH.getIndex()] = args[i];
                        break;
                    case "-o":
                        arr[Flags.OUTPATH.getIndex()] = args[i];
                        break;
                    case "-kp":
                        arr[Flags.KNOWNPATH.getIndex()] = args[i];
                        break;
                    case "-kc":
                        arr[Flags.CRYPTEDPATH.getIndex()] = args[i];
                        break;
                }
            }
        }
        return arr;
    }
}
