public class Lasagna {
    final static int EXPECTED_MINUTES_IN_OVEN = 40;
    final static int PREPARATION_TIME_PER_LAYER = 2;

    public int expectedMinutesInOven() {
        return EXPECTED_MINUTES_IN_OVEN;
    }

    public int remainingMinutesInOven(int minutesInTheOven) {
        return EXPECTED_MINUTES_IN_OVEN - minutesInTheOven;
    }

    public int preparationTimeInMinutes(int numLayers) {
        return numLayers * PREPARATION_TIME_PER_LAYER;
    }

    public int totalTimeInMinutes(int numLayers, int minutesInTheOven) {
        return preparationTimeInMinutes(numLayers) + minutesInTheOven;
    }
}
