package minimumswapstomakestringsequal

import (
	"testing"
)

func Test_isMonotonic(t *testing.T) {
	type args struct {
		A string
		B string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			"",
			args{"xxyyxyxyxx", "xyyxyxxxyx"},
			4,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := minimumSwap(tt.args.A, tt.args.B); got != tt.want {
				t.Errorf("minimumSwap() = %v, want %v", got, tt.want)
			}
		})
	}
}
