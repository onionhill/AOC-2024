open(my $fh, '<', 'input.txt') or die "Could not open file 'input.txt' $!";
print eval join('+', map { /do\(\)/ ? $include = 1 : /don't\(\)/ ? $include = 0 : $include ? /mul\(\d+,\d+\)/g : () } split(/(don't\(\)|do\(\))/, <$fh>)) =~ s/\+1|\+0|1\+//gr;
sub mul { $_[0] * $_[1] }
