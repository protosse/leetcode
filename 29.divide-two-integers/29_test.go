package divideTwoIntegers

import (
	"testing"
)

func Test_divide(t *testing.T) {
	type args struct {
		A int
		B int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			"",
			args{10, 3},
			3,
		},
		{
			"",
			args{-2147483648, 1},
			-2147483648,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := divide(tt.args.A, tt.args.B); got != tt.want {
				t.Errorf("minimumSwap() = %v, want %v", got, tt.want)
			}
		})
	}
}
