/**
 * Created by Daniel on 18-Apr-17.
 */
public enum Flags {
    ALGORITHM(0), ACTION(1), INPATH(2),
    KEYPATH(3), INITPATH(4), OUTPATH(5),
    KNOWNPATH(6), CRYPTEDPATH(7);

    private int value;
    private Flags(int value) {
        this.value = value;
    }

    public int getIndex() {
        return value;
    }
}
