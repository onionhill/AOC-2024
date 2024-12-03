open(my $fh, '<', 'input.txt') or die "Could not open file 'sample.txt' $!";
while (my $line = <$fh>) {
    print eval join('+', $line =~ /mul\(\d+,\d+\)/g);
}
sub mul { $_[0] * $_[1] }
