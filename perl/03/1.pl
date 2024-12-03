open(my $fh, '<', 'input.txt') or die "Could not open file 'input.txt' $!";
print eval join('+',  <$fh> =~ /mul\(\d+,\d+\)/g);
sub mul { $_[0] * $_[1] }
