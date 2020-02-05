package br.com.omni.dojo;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

public class ExampleImplTest {

    private ExampleImpl example;

    @BeforeEach
    public void startedClass() {
        example = new ExampleImpl();
    }

    @Test
    @DisplayName("This test expected this sun two values")
    public void validSum() {
        int expectedValue = 10;

        int resultValue = example.sum(5, 5);

        assertThat(resultValue)
                .isPositive()
                .isEqualTo(expectedValue);
    }

    @Test
    @DisplayName("This test expected this sun positive and negative")
    public void invalidSum() {
        int expectedValue = -5;

        int resultValue = example.sum(5, -10);

        assertThat(resultValue)
                .isNegative()
                .isEqualTo(expectedValue);
    }

}