import Data.List
import Data.Char
import Data.Maybe
import Control.Monad

import qualified Data.ByteString.Char8 as B

readD :: B.ByteString -> Double
readD = fromInteger . fst . fromJust . B.readInteger

readI :: B.ByteString -> Int
readI = fst . fromJust . B.readInt

showD :: Double -> B.ByteString
showD n = B.pack $ show iPart ++ '.' : fDigs
  where
    (iPart, fPart) = quotRem (round (10000 * n)) 10000
    fDigs = let s = show fPart
            in  replicate (4 - length s) '0' ++ s

showI :: Int -> B.ByteString
showI =  B.pack . show

main = B.getContents >>=
  mapM_ (B.putStrLn . showD . sqrt) . reverse . map readD . B.words